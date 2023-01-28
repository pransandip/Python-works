from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QStackedWidget
from src import contstants
from src.components import Buttons
from src.components.Keyboard import keyboard
import datetime

for line in open(contstants.CONFIG, "r"):
    exec(line.strip())

class ButtonData:
    def __init__(self, button, id, name, index):
        self.button = button
        self.id = id
        self.name = name
        self.index = index

class BaseLayout(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.sup_langs: dict = contstants.LANGUAGE_STORE
        self.setupUi()
            
    def screen_buttons(self, parent):
        self.homeButton = Buttons.HomeButton(parent)
        self.backButton = Buttons.BackButton(parent)
        self.nextButton = Buttons.NextButton(parent)

    def keyboard_ui(self):
        keyboard(self)




def init():
    global widget
    global lang, nowRunning, thisWINDOW, barcode_number, TOKEN, post_headers, get_headers
    widget = QStackedWidget()
    lang = "en"
    nowRunning = False
    thisWINDOW = None
    barcode_number = None
    TOKEN = ""
    post_headers = {
                "Content-Type": "application/json",
            }
    get_headers = {}
    global firstweight_data, weight, time, date, alibi_nr, datetime, contract_details
    firstweight_data = {}
    weight = ''
    time = ''
    date = ''
    alibi_nr = ''
    datetime = ""
    contract_details = ""

    global secondweight_data, weight_type, img_string, process_direction, vehicle_details, RED, HOME
    secondweight_data = {}
    weight_type = "first"
    img_string = ""
    process_direction = "0"
    vehicle_details = {}
    RED = False
    HOME = True

    global HOST_DEV, PORT_DEV, HOST, PORT, BASE_URL, PLATEC, IMAGEC
    HOST_DEV = HOST_DEV
    PORT_DEV = PORT_DEV
    HOST = HOST
    PORT = PORT
    BASE_URL = BASE_URL
    PLATEC = PLATEC
    IMAGEC = IMAGEC

    global IMAGE_CAMERA, CAMERA, WAIT_TIME, OLD, WEIGHT_SCREEN, ANPR_URL
    IMAGE_CAMERA = IMAGE_CAMERA
    CAMERA = CAMERA
    WAIT_TIME = WAIT_TIME
    OLD = OLD
    WEIGHT_SCREEN = WEIGHT_SCREEN
    ANPR_URL = ANPR_URL
    
    global PRINT_ALLOWED, PRINTER, TARASAVE, LAST_PAGE_TIME, BASE_URL2, WINDOWS_PRINTER, PRINTER_NAME
    PRINT_ALLOWED = PRINT_ALLOWED
    PRINTER = PRINTER
    TARASAVE = TARASAVE
    LAST_PAGE_TIME = LAST_PAGE_TIME
    BASE_URL2 = BASE_URL2
    WINDOWS_PRINTER = WINDOWS_PRINTER
    PRINTER_NAME = PRINTER_NAME


    
