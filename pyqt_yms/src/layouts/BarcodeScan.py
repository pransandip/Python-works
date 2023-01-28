from PyQt5 import QtWidgets, QtCore, QtGui
from src import contstants
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language, ConnectionError, DisplayError, License, Weighing, ProcessDirection, Signature, NoQR
import datetime, _thread, os, time, gc
from src.components.GetData import get_contract, get_number_plate, check_plate, get_weight, get_vehicle
from src.components import Keyboard as keys





class BarcodeScan(BaseLayout.BaseLayout):
    def __init__(self):
        super(BarcodeScan, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        _thread.start_new_thread(self.getBarcode, (self.nextButton,))
        # _thread.start_new_thread(self.check_focus, ())
        self.next_timer = QtCore.QTimer()
        self.next_timer.timeout.connect(lambda: self.check_focus())
        self.next_timer.setSingleShot(True)
        self.next_timer.start(1000)
        # QtCore.QTimer.singleShot(1000, lambda: self.check_focus())
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())


    def check_focus(self):
        time.sleep(0.5)
        while True:
            if self.barcodeScanCheck.hasFocus() == False:
                self.focus()
            else:
                self.next_timer
                break
    
    def focus(self):
        self.barcodeScanCheck.setFocus(True)


    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()
        self.screen_buttons(self.centralwidget)

        self.headerLabel = QtWidgets.QLabel(self.centralwidget)
        self.headerLabel.setGeometry(QtCore.QRect(260, 100, 600, 70))
        self.headerLabel.setStyleSheet("border-bottom:2px solid #000947;\n"
"color:#000947;\n"
"font: 28pt \"Arial\";\n"
"padding:0px;\n"
"font-weight:bold;\n"
"border-radius:15px")
        self.headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLabel.setObjectName("headerLabel")
        self.holdBarcodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.holdBarcodeLabel.setGeometry(QtCore.QRect(430, 300, 701, 131))
        self.holdBarcodeLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.holdBarcodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.holdBarcodeLabel.setObjectName("holdBarcodeLabel")
        self.orLabel = QtWidgets.QLabel(self.centralwidget)
        self.orLabel.setGeometry(QtCore.QRect(0, 540, 1021, 41))
        self.orLabel.setStyleSheet("font: 16pt \"Arial\";")
        self.orLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.orLabel.setObjectName("orLabel")
        self.manualButton = QtWidgets.QPushButton(self.centralwidget)
        self.manualButton.setGeometry(QtCore.QRect(360, 610, 301, 71))
        self.manualButton.setStyleSheet("background-color:#000947;\n"
"color:#fff;\n"
"font: 18pt \"Arial\";\n"
"border-radius:15px")
        self.manualButton.setObjectName("manualButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 280, 351, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "reader1.jpeg")))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.barcodeScanCheck = QtWidgets.QLineEdit(self.centralwidget)
        self.barcodeScanCheck.setGeometry(QtCore.QRect(550, 470, 441, 51))
        self.barcodeScanCheck.setStyleSheet("font: 13pt;background-color:#fff;border:1px solid black;border-radius:20px;padding:5px;")
        self.barcodeScanCheck.setObjectName("barcodeScanCheck")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.nextButton.hide()
        self.backButton.hide()

        self.manualButton.clicked.connect(self.manual)
        self.homeButton.clicked.connect(self.gotohome)
        self.nextButton.clicked.connect(self.next)
        self.barcodeScanCheck.setText("")


    def getBarcode(self, next_button):
        try:
            time.sleep(1)
            barcode_len = -1
            while True:
                if BaseLayout.thisWINDOW != self:
                    _thread.exit()
                if len(self.barcodeScanCheck.text()) == barcode_len:
                    break
                time.sleep(1)
                if len(self.barcodeScanCheck.text()) > 0:
                    barcode_len = len(self.barcodeScanCheck.text())
            BaseLayout.barcode_number = str(self.barcodeScanCheck.text())
            next_button.click()
            _thread.exit()
        except:
            pass

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headerLabel.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["barcode_scan"]))
        self.holdBarcodeLabel.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["hold_barcode_infront"]))
        self.orLabel.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["or"]))
        self.manualButton.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["enter_barcode_manually"]))
    
    def gotohome(self):
        if BaseLayout.thisWINDOW == self:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language.Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()   
        else:
            return
    
    def manual(self):
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(ManualEnter())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        # self.deleteLater()
        return

    def next(self):
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(BarcodeWait())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()
        return




class BarcodeWait(BaseLayout.BaseLayout):
    def __init__(self):
        super(BarcodeWait, self).__init__()
        self.setupUi()
        QtCore.QTimer.singleShot(3000, lambda: self.getData())

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet(
            "background-color:#fff;\n" 'font: 28pt "Arial";')
        self.centralwidget = HeadTemplate()

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 270, 1021, 161))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def getData(self):
        if BaseLayout.weight_type == "tara_save":
            try:
                res = get_contract(BaseLayout.barcode_number)
                if res["status"] == 200:
                    try:
                        BaseLayout.contract_details = res["data"]
                        if BaseLayout.weight_type == "tara_save":
                            BaseLayout.widget.removeWidget(self)
                            BaseLayout.widget.addWidget(License.ExtractingLicense())
                            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        else:
                            BaseLayout.weight_type = "first"
                            plt = ""
                            try:
                                plate = get_number_plate(BaseLayout.PLATEC)
                                plt = plate["LP Number"].replace("_", " ").replace("-", " ")
                            except:
                                pass
                            BaseLayout.firstweight_data["vehicle"] = plt
                            BaseLayout.widget.removeWidget(self)
                            BaseLayout.widget.addWidget(License.ConfirmLicense())
                            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    except Exception as e:
                        print(e)
                        BaseLayout.firstweight_data["vehicle"] = ""
                        BaseLayout.widget.removeWidget(self)
                        BaseLayout.widget.addWidget(License.ConfirmLicense())
                        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                else:
                    BaseLayout.widget.removeWidget(self)
                    BaseLayout.widget.addWidget(NoQR.DisplayText(contstants.LANGUAGE_STORE[BaseLayout.lang]["id_not_found"]))
                    BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    return
            except Exception as e:
                print(e)
                BaseLayout.widget.removeWidget(self)
                BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        
        else:
        
            if str(BaseLayout.barcode_number)[:2] == "PL":
                try:
                    res = check_plate(str(BaseLayout.barcode_number)[2:])
                    if res:
                        BaseLayout.secondweight_data = res
                        BaseLayout.weight_type = "second"
                        try:
                            res = get_weight("GET WEIGHTNM")
                            BaseLayout.weight = res['weight']
                            BaseLayout.date = res['date']
                            BaseLayout.time = res["time"]
                            BaseLayout.alibi_nr = res['alibi_nr']
                            dt_obj = BaseLayout.date + " " + BaseLayout.time
                            BaseLayout.datetime = datetime.datetime.strptime(dt_obj, "%d.%m.%y %H:%M")
                            
                            BaseLayout.widget.removeWidget(self)
                            if BaseLayout.WEIGHT_SCREEN:
                                BaseLayout.widget.addWidget(Weighing.WeightPanel())
                            else:
                                BaseLayout.widget.addWidget(Signature.Signature())
                            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        except Exception as e:
                            print(e)
                            BaseLayout.widget.removeWidget(self)
                            BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    else:
                        BaseLayout.widget.removeWidget(self)
                        BaseLayout.widget.addWidget(NoQR.DisplayText(contstants.LANGUAGE_STORE[BaseLayout.lang]["not_in_yard_list"]))
                        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        return
                except Exception as e:
                    print(e)
                    BaseLayout.widget.removeWidget(self)
                    BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                    BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)

            elif str(BaseLayout.barcode_number)[:2] == "TA":
                try:
                    barcode = str(BaseLayout.barcode_number).split("PL")
                    contract_number = barcode[0][2:]
                    license_id = barcode[1]
                    res = check_plate(license_id)
                    if res == False:
                        res = get_contract(contract_number)
                        if res["status"] == 200:
                            BaseLayout.contract_details = res["data"]
                            res = get_vehicle(license_id)
                            BaseLayout.vehicle_details = res["data"]
                            BaseLayout.weight_type = "tara"
                            try:
                                res = get_weight("GET WEIGHTNM")
                                BaseLayout.weight = res['weight']
                                BaseLayout.date = res['date']
                                BaseLayout.time = res["time"]
                                BaseLayout.alibi_nr = res['alibi_nr']
                                dt_obj = BaseLayout.date + " " + BaseLayout.time
                                BaseLayout.datetime = datetime.datetime.strptime(dt_obj, "%d.%m.%y %H:%M")
                                
                                BaseLayout.widget.removeWidget(self)
                                BaseLayout.widget.addWidget(ProcessDirection.ProcessDirection())
                                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                            except Exception as e:
                                print(e)
                                BaseLayout.widget.removeWidget(self)
                                BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        else:
                            BaseLayout.widget.removeWidget(self)
                            BaseLayout.widget.addWidget(NoQR.DisplayText(contstants.LANGUAGE_STORE[BaseLayout.lang]["id_not_found"]))
                            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                            return

                    else:
                        BaseLayout.widget.removeWidget(self)
                        BaseLayout.widget.addWidget(NoQR.DisplayText(contstants.LANGUAGE_STORE[BaseLayout.lang]["already_in_list"]))
                        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        return

                except Exception as e:
                    print(e)
                    BaseLayout.widget.removeWidget(self)
                    BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                    BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)

            else:
                try:
                    res = get_contract(BaseLayout.barcode_number)
                    if res["status"] == 200:
                        try:
                            BaseLayout.contract_details = res["data"]
                            if BaseLayout.weight_type == "tara_save":
                                BaseLayout.widget.removeWidget(self)
                                BaseLayout.widget.addWidget(License.ExtractingLicense())
                                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                            else:
                                BaseLayout.weight_type = "first"
                                plt = ""
                                try:
                                    plate = get_number_plate(BaseLayout.PLATEC)
                                    plt = plate["LP Number"].replace("_", " ").replace("-", " ")
                                except:
                                    pass
                                BaseLayout.firstweight_data["vehicle"] = plt
                                BaseLayout.widget.removeWidget(self)
                                BaseLayout.widget.addWidget(License.ConfirmLicense())
                                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        except Exception as e:
                            print(e)
                            BaseLayout.firstweight_data["vehicle"] = ""
                            BaseLayout.widget.removeWidget(self)
                            BaseLayout.widget.addWidget(License.ConfirmLicense())
                            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    else:
                        BaseLayout.widget.removeWidget(self)
                        BaseLayout.widget.addWidget(NoQR.DisplayText(contstants.LANGUAGE_STORE[BaseLayout.lang]["id_not_found"]))
                        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                        return

                except Exception as e:
                    print(e)
                    BaseLayout.widget.removeWidget(self)
                    BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                    BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()


        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["please_wait"]))




class ManualEnter(BaseLayout.BaseLayout):
    def __init__(self):
        super(ManualEnter, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())

    def setupUi(self):
        self.setObjectName("SafetyInstr")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()
        self.screen_buttons(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000947;\n"
            "color:#fff;\n"
            'font: 16pt "Arial";\n'
            "border-radius:15px\n"
            "}"
        )
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 225, 621, 61))
        self.lineEdit.setStyleSheet(
            'font: 16pt "Arial";\n' "border-radius:15px;\n" "border: 1px solid black;"
        )
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 120, 461, 61))
        self.label.setStyleSheet("border-bottom:2px solid #000947;\n"
"color:#000947;\n"
"font: 22pt \"Arial\";\n"
"padding:0px;\n"
"font-weight:bold;\n"
"border-radius:15px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 330, 761, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QPushButton{"
                                 "border: 1px solid black;\n"
                                 "border-radius: 3px;\n"
                                 "color: #000947;\n"
                                 "background-color: white;}"
                                 )
        self.keyboard_ui()
        self.homeButton.clicked.connect(self.gotohome)
        self.backButton.clicked.connect(self.previous)
        self.nextButton.clicked.connect(self.next)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def key_press(self, text):
        if text == "<-":
            txt = self.lineEdit.text()
            self.lineEdit.setText(txt[:-1])
        else:
            txt = self.lineEdit.text()
            txt += text
            self.lineEdit.setText(txt)

    def gotohome(self):
        if BaseLayout.thisWINDOW == self:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language.Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            return

    def previous(self):
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(BarcodeScan())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()

    def next(self):
        if bool(self.lineEdit.text()):                  
            BaseLayout.barcode_number = self.lineEdit.text()
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(BarcodeWait())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            self.lineEdit.setStyleSheet("color: #000947;\n"
            "border: 1px solid red;\n"
            "font: bold 20px;\n""border-radius:20px;")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["enter_barcode_manually"]))
        keys.keyboard_labels(self, _translate)