import socket
import os, _thread, sys
import requests, json, qrcode, time, codecs
from src.layouts import BaseLayout
from websocket import create_connection
from urllib.parse import urlencode
from PIL.ImageQt import ImageQt
from reportlab.pdfgen import canvas
import win32api
import win32print

def get_token():
    EMAIL = "admin@admin.com"
    PASSWORD = "Woehrl4100"
    headers = {
                "Content-Type": "application/json",
            }
    data = {
        "username": EMAIL,
        "password":PASSWORD
    }
    res = requests.post(url=BaseLayout.BASE_URL+"/api-token-auth", data=json.dumps(data).encode(), headers=headers).json()
    if "token" in res:
        BaseLayout.TOKEN = res["token"]
        BaseLayout.post_headers = {
                "Content-Type": "application/json",
                "Authorization": f"Token {BaseLayout.TOKEN}"
            }

        BaseLayout.get_headers = {
                        "Authorization": f"Token {BaseLayout.TOKEN}"
                    }

    else:
        print("cridential error")
        sys.exit()
    return



def check_connection_timelimit(_):
    while True:
        import time
        time.sleep(5) # salik is the for the can the inside the for the process of the 
        response = requests.get(url=BaseLayout.BASE_URL+f"/api/Warehouse-View/", headers=BaseLayout.get_headers)
        if int(response.status_code) == 200:
            global nowRunning
            nowRunning = True
            _thread.exit()
        else:
            continue


def get_contract(number):
    res = requests.get(url=BaseLayout.BASE_URL+f"/api/Contract/{number}/", headers=BaseLayout.get_headers, timeout=15)
    return {"status":res.status_code, "data":res.json()}

def get_number_plate(cmd):
    url = BaseLayout.ANPR_URL + "/camera"
    payload={"c_idx":int(cmd)}
    headers = {}
    response = requests.request("GET", url= url, params=payload)
    print(response.json())
    return response.json()
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.settimeout(15)
    #     s.connect((BaseLayout.HOST_DEV, BaseLayout.PORT_DEV))
    #     s.sendall(cmd.encode("UTF-8"))
    #     data = s.recv(1024)
    #     retval = data.decode("UTF-8")
    #     w_obj = json.loads(retval)
    #     return w_obj
    # ws = create_connection(f"ws://{BaseLayout.HOST_DEV}:{BaseLayout.PORT_DEV}", timeout=15)
    # result =  ws.recv()
    # ws.send(cmd)
    # result =  ws.recv()
    # ws.close()
    # jobj = json.loads(result)
    # return jobj


def check_vehicle(plate):
    lp = urlencode({"license_plate": plate})
    res = requests.get(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/?{lp}", headers=BaseLayout.get_headers, timeout=15).json()
    if len(res) > 0:
        vehicle_id = res[0]['id']
        res = requests.get(url=BaseLayout.BASE_URL+f"/api/Transactions/?vehicle={vehicle_id}&trans_flag=0", headers=BaseLayout.get_headers, timeout=15).json()
        if len(res) > 0:
            return True
        else:
            return False
    else:
        return False


def get_weight(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(15)
        s.connect((BaseLayout.HOST_DEV, BaseLayout.PORT_DEV))
        s.sendall(cmd.encode("UTF-8"))
        data = s.recv(1024)
        retval = data.decode("UTF-8")
        w_obj = json.loads(retval)
        return w_obj
    # ws = create_connection(f"ws://{BaseLayout.HOST_DEV}:{BaseLayout.PORT_DEV}", timeout=20)
    # result =  ws.recv()
    # ws.send(cmd)
    # result =  ws.recv()
    # ws.close()
    # jobj = json.loads(result)
    # if jobj["state"] == "bad":
    #     ws = create_connection(f"ws://{BaseLayout.HOST_DEV}:{BaseLayout.PORT_DEV}", timeout=20)
    #     result =  ws.recv()
    #     ws.send(cmd)
    #     result =  ws.recv()
    #     ws.close()
    #     jobj = json.loads(result)
    #     return jobj
    # else:
    #     return jobj


def get_image(cmd):
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.settimeout(15)
    #     s.connect((HOST_DEV, PORT_DEV))
    #     s.sendall(cmd.encode("UTF-8"))
    #     data = ""
    #     while True:
    #         part = s.recv(1024)
    #         if len(part) == 0:
    #             break
    #         else:
    #             data += part.decode("UTF-8")
    #     print(data)
    #     jobj = json.loads(data)
    #     time.sleep(2)
    # ws = create_connection(f"ws://{HOST_DEV}:{PORT_DEV}", timeout=20)
    # result =  ws.recv()
    # ws.send(cmd)
    # result =  ws.recv()
    # ws.close()
    # jobj = json.loads(result)
    # return jobj
    res = requests.get(url=BaseLayout.BASE_URL2+f"/scale_data/?cmd=GET%20IMAGE{cmd}", headers=BaseLayout.get_headers, timeout=15).json()
    return res



def send_first_weight():
    license_id = ""
    license_plate = urlencode({"license_plate": BaseLayout.firstweight_data["vehicle"]})
    res = requests.get(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/?{license_plate}", headers=BaseLayout.get_headers, timeout=15).json()
    if len(res) == 0:
        license_data = {"license_plate": BaseLayout.firstweight_data["vehicle"]}
        res = requests.post(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/", data=json.dumps(license_data).encode(), headers=BaseLayout.post_headers).json()
        license_id = res["id"]
    else:
        license_id = res[0]["id"]
    sup_id = ""
    if len(BaseLayout.contract_details["supplier"]) > 0:
        sup_id = BaseLayout.contract_details["supplier"][0]["id"]
    else:
        sup_id = None
    tras_data = {
                "first_weight": BaseLayout.weight,
                'vehicle': license_id,
                'article': BaseLayout.contract_details["required_materials"][0]["material"]["id"],
                'customer': BaseLayout.contract_details["customer"]["id"],
                'supplier': sup_id,
                "net_weight": BaseLayout.weight,
                "contract_number": BaseLayout.contract_details["contract_number"],
                "firstw_date_time": str(BaseLayout.datetime.date())+"T"+str(BaseLayout.datetime.time())+"Z",
                "firstw_alibi_nr": BaseLayout.alibi_nr.replace(" ", ""),
                "trans_flag": 0,
                "yard": 1
            }
    res = requests.post(url=BaseLayout.BASE_URL+f'/api/Transactions/', data=json.dumps(tras_data).encode(), headers=BaseLayout.post_headers, timeout=15).json()
    
    _thread.start_new_thread(save_images_first, (res,))

    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=10,
                        border=4,
                    )
    qr_data = "PL"+str(license_id)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qimage = ImageQt(img)
    img.save("HoffticketQR.png")
    COOL_PDF_FILE = ("Hoffticket.pdf")
    pdf = canvas.Canvas(COOL_PDF_FILE)
    pdf.setFont('Helvetica', 30)
    pdf.drawString(225, 800, "Hoffticket")
    pdf.setFont('Helvetica', 30)
    pdf.drawString(235, 475, qr_data)
    pdf.setFont('Helvetica', 30)
    pdf.drawString(100, 425, "Bitte verwenden Sie diesen")
    pdf.setFont('Helvetica', 30)
    pdf.drawString(80, 375, "QR-Code für die Zweitwiegung")
    pdf.drawImage("HoffticketQR.png", 150, 500)
    pdf.save()
    
    if BaseLayout.PRINT_ALLOWED:
        time.sleep(2)
        if BaseLayout.WINDOWS_PRINTER:
            file_name = "Hoffticket.pdf"
            _thread.start_new_thread(print_pdf, (file_name,))
        else:
            os.system(f"lp -d {BaseLayout.PRINTER} Hoffticket.pdf")
    return True


def save_images_first(res):
    if BaseLayout.CAMERA == 1:
        IMAGE_1,IMAGE_2 = None, None
        try:
            IMAGE = get_image(BaseLayout.IMAGE_CAMERA[0])
            IMAGE_1 = IMAGE["image_data"]
        except:
            pass
        time.sleep(1)
        try:
            IMAGE = get_image(BaseLayout.IMAGE_CAMERA[1])
            IMAGE_2 = IMAGE["image_data"]
        except:
            pass
        image_data = {
            "image1": IMAGE_1,
            "image2": IMAGE_2,
            "transaction": res["id"]
        }
        requests.post(url=BaseLayout.BASE_URL+f'/api/SaveBase64/', data=json.dumps(image_data).encode(), headers=BaseLayout.post_headers, timeout=15).json()


def check_plate(LICENSE_ID):
    res = requests.get(url=BaseLayout.BASE_URL+f"/api/transact/?vehicle={LICENSE_ID}&trans_flag=0", headers=BaseLayout.get_headers)
    if res.status_code == 200:
        res = res.json()
        if len(res) > 0:
            return res[0]
        else:
            return False
    else:
        return False



def send_second_weight():
    tras_data = {
                "second_weight": BaseLayout.weight,
                "net_weight": abs(
                    int(BaseLayout.weight.replace(" ", ""))
                    - int(BaseLayout.secondweight_data["first_weight"].replace(" ", ""))
                ),
                "secondw_date_time": str(BaseLayout.datetime.date())+ "T" + str(BaseLayout.datetime.time()) + "Z",
                "secondw_alibi_nr": BaseLayout.alibi_nr.replace(" ", ""),
                "trans_flag": 1,
                "yard": 1,
            }
    secondweight_data = requests.put(url=BaseLayout.BASE_URL+f'/api/Transactions/{BaseLayout.secondweight_data["id"]}/', data=json.dumps(tras_data).encode(), headers=BaseLayout.post_headers, timeout=15).json()
    
    sign_data = {
                "image": BaseLayout.img_string,
                "transaction_id": secondweight_data['id']
            }
    requests.post(url=BaseLayout.BASE_URL+f'/api/DriverSign/', data=json.dumps(sign_data).encode(), headers=BaseLayout.post_headers, timeout=15)

    pdf_data = {
                "id": secondweight_data['id'],
                "username": ""
            }
    res = requests.post(url=BaseLayout.BASE_URL+f'/api/Pdf_lieferscheine_print/', data=json.dumps(pdf_data).encode(), headers=BaseLayout.post_headers, timeout=15).json()

    if BaseLayout.PRINT_ALLOWED:
        pdffile = open("myfile.pdf", "wb")
        pdffile.write(codecs.decode(
            res["pdf"].encode(), "base64"))
        pdffile.close()
        if BaseLayout.WINDOWS_PRINTER:
            file_name = "myfile.pdf"
            _thread.start_new_thread(print_pdf, (file_name,))
        else:
            os.system(f"lp -d {BaseLayout.PRINTER} myfile.pdf")
    return True


def save_vehicle_weight():
    license_id = ""
    license_data = {
                    "license_plate": BaseLayout.firstweight_data["vehicle"],
                    "vehicle_weight": BaseLayout.weight,
                    "vehicle_weight_id": BaseLayout.alibi_nr.replace(" ", ""),
                    "vehicle_weight_date": str(BaseLayout.datetime.date()),
                    "vehicle_weight_time": str(BaseLayout.datetime.time()),
                    "self_tara": True,
                    }
    if BaseLayout.firstweight_data["VEHICLE_ID"] == None:            
        res = requests.post(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/", data=json.dumps(license_data).encode(), headers=BaseLayout.post_headers).json()
        license_id = res["id"]
    else:
        license_id = BaseLayout.firstweight_data["VEHICLE_ID"]
        res = requests.put(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/{license_id}/", data=json.dumps(license_data).encode(), headers=BaseLayout.post_headers).json()
    
    qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
    qr_data = "TA" + str(BaseLayout.contract_details["contract_number"]) + "PL" + str(license_id)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qimage = ImageQt(img)
    img.save("TaraticketQR.png")
    COOL_PDF_FILE = ("Taraticket.pdf")
    pdf = canvas.Canvas(COOL_PDF_FILE)
    pdf.setFont('Helvetica', 30)
    pdf.drawString(225, 800, "Taraticket")
    pdf.setFont('Helvetica', 30)
    pdf.drawString(200, 475, qr_data)
    pdf.setFont('Helvetica', 30)
    pdf.drawString(100, 425, "Bitte verwenden Sie diesen")
    pdf.setFont('Helvetica', 30)
    pdf.drawString(80, 375, "QR-Code für die Tarawiegung")
    pdf.drawImage("TaraticketQR.png", 150, 500)
    pdf.save()
    if BaseLayout.PRINT_ALLOWED:
        time.sleep(2)
        if BaseLayout.WINDOWS_PRINTER:
            file_name = "Taraticket.pdf"
            _thread.start_new_thread(print_pdf, (file_name,))
        else:
            os.system(f"lp -d {BaseLayout.PRINTER} Taraticket.pdf")
    
    return True


def get_vehicle(vehicle_id):
    res = requests.get(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/{vehicle_id}/", headers=BaseLayout.get_headers, timeout=15)
    return {"status":res.status_code, "data":res.json()}



def send_tara_weight():
    sup_id = ""
    tras_data = {}
    if len(BaseLayout.contract_details["supplier"]) > 0:
        sup_id = BaseLayout.contract_details["supplier"][0]["id"]
    else:
        sup_id = None
    if int(BaseLayout.process_direction) == 0:
        tras_data = {
            "contract_number" : BaseLayout.contract_details["contract_number"],
            "vehicle": BaseLayout.vehicle_details["id"],
            "article": BaseLayout.contract_details["required_materials"][0]["material"]["id"],
            "customer": BaseLayout.contract_details["customer"]["id"],
            "supplier": sup_id,
            "second_weight": str(BaseLayout.vehicle_details["vehicle_weight"]),
            "first_weight": BaseLayout.weight,
            "net_weight": abs(int(BaseLayout.weight.replace(" ", "")) - BaseLayout.vehicle_details["vehicle_weight"]),
            "secondw_date_time": BaseLayout.vehicle_details["vehicle_weight_date"]+"T"+BaseLayout.vehicle_details["vehicle_weight_time"]+"Z",
            "firstw_date_time": str(BaseLayout.datetime.date()) + "T" + str(BaseLayout.datetime.time()) + "Z",
            "secondw_alibi_nr": BaseLayout.vehicle_details["vehicle_weight_id"],
            "firstw_alibi_nr": BaseLayout.alibi_nr.replace(" ", ""),
            "vehicle_second_weight_flag": 1,
            "status": BaseLayout.process_direction,
            "trans_flag": 1,
            "yard": 1,
        }
    else:
        tras_data = {
            "contract_number" : BaseLayout.contract_details["contract_number"],
            "vehicle": BaseLayout.vehicle_details["id"],
            "article": BaseLayout.contract_details["required_materials"][0]["material"]["id"],
            "customer": BaseLayout.contract_details["customer"]["id"],
            "supplier": sup_id,
            "first_weight": str(BaseLayout.vehicle_details["vehicle_weight"]),
            "second_weight": BaseLayout.weight,
            "net_weight": abs(int(BaseLayout.weight.replace(" ", "")) - BaseLayout.vehicle_details["vehicle_weight"]),
            "firstw_date_time": BaseLayout.vehicle_details["vehicle_weight_date"]+"T"+BaseLayout.vehicle_details["vehicle_weight_time"]+"Z",
            "secondw_date_time": str(BaseLayout.datetime.date()) + "T" + str(BaseLayout.datetime.time()) + "Z",
            "firstw_alibi_nr": BaseLayout.vehicle_details["vehicle_weight_id"],
            "secondw_alibi_nr": BaseLayout.alibi_nr.replace(" ", ""),
            "vehicle_weight_flag": 1,
            "status": BaseLayout.process_direction,
            "trans_flag": 1,
            "yard": 1,
        }

    secondweight_data = requests.post(url=BaseLayout.BASE_URL+f'/api/Transactions/', data=json.dumps(tras_data).encode(), headers=BaseLayout.post_headers, timeout=15).json()
    
    _thread.start_new_thread(save_images_first, (secondweight_data,))
    
    sign_data = {
                "image": BaseLayout.img_string,
                "transaction_id": secondweight_data['id']
            }
    requests.post(url=BaseLayout.BASE_URL+f'/api/DriverSign/', data=json.dumps(sign_data).encode(), headers=BaseLayout.post_headers, timeout=15)

    pdf_data = {
                "id": secondweight_data['id'],
                "username": ""
            }
    res = requests.post(url=BaseLayout.BASE_URL+f'/api/Pdf_lieferscheine_print/', data=json.dumps(pdf_data).encode(), headers=BaseLayout.post_headers, timeout=15).json()

    if BaseLayout.PRINT_ALLOWED:
        pdffile = open("myfile.pdf", "wb")
        pdffile.write(codecs.decode(
            res["pdf"].encode(), "base64"))
        pdffile.close()
        if BaseLayout.WINDOWS_PRINTER:
            file_name = "myfile.pdf"
            _thread.start_new_thread(print_pdf, (file_name,))
        else:
            os.system(f"lp -d {BaseLayout.PRINTER} myfile.pdf")
    return True

# def change_lights(_):
#     while True:
#         if BaseLayout.HOME:
#             if BaseLayout.RED:
#                 try:
#                     print("green on")
#                     requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT4%20OFF", headers=BaseLayout.get_headers, timeout=5)
#                     time.sleep(1)
#                     requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT3%20ON", headers=BaseLayout.get_headers, timeout=5)
#                 except:
#                     pass
#         else:
#             if not BaseLayout.RED:
#                 try:
#                     print("red on")
#                     requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT3%20OFF", headers=BaseLayout.get_headers, timeout=5)
#                     time.sleep(1)
#                     requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT4%20ON", headers=BaseLayout.get_headers, timeout=5)
#                 except:
#                     pass
            

def green_on(_):
    try:
        requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT4%20OFF", headers=BaseLayout.get_headers, timeout=5)
        time.sleep(1)
        requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT3%20ON", headers=BaseLayout.get_headers, timeout=5)
    except:
        pass
    _thread.exit()

def red_on(_):
    try:
        requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT3%20OFF", headers=BaseLayout.get_headers, timeout=5)
        time.sleep(1)
        requests.get(url=BaseLayout.BASE_URL+f"/scale_data/?cmd=OUT4%20ON", headers=BaseLayout.get_headers, timeout=5)
    except:
        pass
    _thread.exit()


def default_global():
    BaseLayout.secondweight_data = {}
    BaseLayout.weight_type = "first"
    BaseLayout.img_string = ""
    BaseLayout.process_direction = "0"
    BaseLayout.vehicle_details = {}
    BaseLayout.firstweight_data = {}
    BaseLayout.weight = ''
    BaseLayout.time = ''
    BaseLayout.date = ''
    BaseLayout.alibi_nr = ''
    BaseLayout.datetime = ""
    BaseLayout.contract_details = ""


def print_pdf(file_name):
    print("printing")
    win32print.SetDefaultPrinter(BaseLayout.PRINTER_NAME)
    printer = win32print.GetDefaultPrinter()
    print(printer)
    win32api.ShellExecute(0, "print", file_name, None, ".", 0)
    print("printing done")
    _thread.exit()