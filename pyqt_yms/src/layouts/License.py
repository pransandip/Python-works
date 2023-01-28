from PyQt5 import QtWidgets, QtCore, QtGui
from src import contstants
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, BarcodeScan, Language, ConnectionError, Weighing, DisplayError
import datetime, _thread, os, time, requests
from src.components import Keyboard as keys
from src.components.GetData import check_vehicle, get_weight
from PyQt5.QtCore import Qt

class ConfirmLicense(BaseLayout.BaseLayout):
    def __init__(self):
        super(ConfirmLicense, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())

    def setupUi(self):
        self.setObjectName("language")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.screen_buttons(self.centralwidget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 360, 761, 281))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.PButton = QtWidgets.QPushButton(self.frame)
        self.PButton.setGeometry(QtCore.QRect(630, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.PButton.setFont(font)
        self.PButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.PButton.setObjectName("PButton")
        self.Button_5 = QtWidgets.QPushButton(self.frame)
        self.Button_5.setGeometry(QtCore.QRect(280, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_5.setObjectName("Button_5")
        self.ButtonGerO = QtWidgets.QPushButton(self.frame)
        self.ButtonGerO.setGeometry(QtCore.QRect(630, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonGerO.setFont(font)
        self.ButtonGerO.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.ButtonGerO.setObjectName("ButtonGerO")
        self.GButton = QtWidgets.QPushButton(self.frame)
        self.GButton.setGeometry(QtCore.QRect(280, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.GButton.setFont(font)
        self.GButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.GButton.setObjectName("GButton")
        self.Button_7 = QtWidgets.QPushButton(self.frame)
        self.Button_7.setGeometry(QtCore.QRect(420, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_7.setObjectName("Button_7")
        self.YButton = QtWidgets.QPushButton(self.frame)
        self.YButton.setGeometry(QtCore.QRect(350, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.YButton.setFont(font)
        self.YButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.YButton.setObjectName("YButton")
        self.TButton = QtWidgets.QPushButton(self.frame)
        self.TButton.setGeometry(QtCore.QRect(280, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.TButton.setFont(font)
        self.TButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.TButton.setObjectName("TButton")
        self.WButton = QtWidgets.QPushButton(self.frame)
        self.WButton.setGeometry(QtCore.QRect(70, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.WButton.setFont(font)
        self.WButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.WButton.setObjectName("WButton")
        self.UButton = QtWidgets.QPushButton(self.frame)
        self.UButton.setGeometry(QtCore.QRect(420, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.UButton.setFont(font)
        self.UButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.UButton.setObjectName("UButton")
        self.XButton = QtWidgets.QPushButton(self.frame)
        self.XButton.setGeometry(QtCore.QRect(70, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.XButton.setFont(font)
        self.XButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.XButton.setObjectName("XButton")
        self.QButton = QtWidgets.QPushButton(self.frame)
        self.QButton.setGeometry(QtCore.QRect(0, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.QButton.setFont(font)
        self.QButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.QButton.setObjectName("QButton")
        self.BButton = QtWidgets.QPushButton(self.frame)
        self.BButton.setGeometry(QtCore.QRect(280, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.BButton.setFont(font)
        self.BButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.BButton.setObjectName("BButton")
        self.DButton = QtWidgets.QPushButton(self.frame)
        self.DButton.setGeometry(QtCore.QRect(140, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.DButton.setFont(font)
        self.DButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.DButton.setObjectName("DButton")
        self.IButton = QtWidgets.QPushButton(self.frame)
        self.IButton.setGeometry(QtCore.QRect(490, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.IButton.setFont(font)
        self.IButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.IButton.setObjectName("IButton")
        self.Button_9 = QtWidgets.QPushButton(self.frame)
        self.Button_9.setGeometry(QtCore.QRect(560, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_9.setObjectName("Button_9")
        self.backButton_2 = QtWidgets.QPushButton(self.frame)
        self.backButton_2.setGeometry(QtCore.QRect(490, 210, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.backButton_2.setFont(font)
        self.backButton_2.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.backButton_2.setObjectName("backButton_2")
        self.VButton = QtWidgets.QPushButton(self.frame)
        self.VButton.setGeometry(QtCore.QRect(210, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.VButton.setFont(font)
        self.VButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.VButton.setObjectName("VButton")
        self.ZButton = QtWidgets.QPushButton(self.frame)
        self.ZButton.setGeometry(QtCore.QRect(0, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.ZButton.setFont(font)
        self.ZButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.ZButton.setObjectName("ZButton")
        self.ButtonGerA = QtWidgets.QPushButton(self.frame)
        self.ButtonGerA.setGeometry(QtCore.QRect(700, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonGerA.setFont(font)
        self.ButtonGerA.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.ButtonGerA.setObjectName("ButtonGerA")
        self.AButton = QtWidgets.QPushButton(self.frame)
        self.AButton.setGeometry(QtCore.QRect(0, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.AButton.setFont(font)
        self.AButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.AButton.setObjectName("AButton")
        self.Button_6 = QtWidgets.QPushButton(self.frame)
        self.Button_6.setGeometry(QtCore.QRect(350, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_6.setObjectName("Button_6")
        self.RButton = QtWidgets.QPushButton(self.frame)
        self.RButton.setGeometry(QtCore.QRect(210, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.RButton.setFont(font)
        self.RButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.RButton.setObjectName("RButton")
        self.HButton = QtWidgets.QPushButton(self.frame)
        self.HButton.setGeometry(QtCore.QRect(350, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.HButton.setFont(font)
        self.HButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.HButton.setObjectName("HButton")
        self.Button_2 = QtWidgets.QPushButton(self.frame)
        self.Button_2.setGeometry(QtCore.QRect(70, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_2.setObjectName("Button_2")
        self.Button_1 = QtWidgets.QPushButton(self.frame)
        self.Button_1.setGeometry(QtCore.QRect(0, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_1.setFont(font)
        self.Button_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        self.MButton = QtWidgets.QPushButton(self.frame)
        self.MButton.setGeometry(QtCore.QRect(420, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.MButton.setFont(font)
        self.MButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.MButton.setObjectName("MButton")
        self.Button_0 = QtWidgets.QPushButton(self.frame)
        self.Button_0.setGeometry(QtCore.QRect(630, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_0.setObjectName("Button_0")
        self.ButtonGerU = QtWidgets.QPushButton(self.frame)
        self.ButtonGerU.setGeometry(QtCore.QRect(700, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonGerU.setFont(font)
        self.ButtonGerU.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.ButtonGerU.setObjectName("ButtonGerU")
        self.FButton = QtWidgets.QPushButton(self.frame)
        self.FButton.setGeometry(QtCore.QRect(210, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.FButton.setFont(font)
        self.FButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.FButton.setObjectName("FButton")
        self.EButton = QtWidgets.QPushButton(self.frame)
        self.EButton.setGeometry(QtCore.QRect(140, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.EButton.setFont(font)
        self.EButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.EButton.setObjectName("EButton")
        self.SButton = QtWidgets.QPushButton(self.frame)
        self.SButton.setGeometry(QtCore.QRect(70, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.SButton.setFont(font)
        self.SButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.SButton.setObjectName("SButton")
        self.Button_4 = QtWidgets.QPushButton(self.frame)
        self.Button_4.setGeometry(QtCore.QRect(210, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_4.setObjectName("Button_4")
        self.Button_8 = QtWidgets.QPushButton(self.frame)
        self.Button_8.setGeometry(QtCore.QRect(490, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_8.setObjectName("Button_8")
        self.NButton = QtWidgets.QPushButton(self.frame)
        self.NButton.setGeometry(QtCore.QRect(350, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.NButton.setFont(font)
        self.NButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.NButton.setObjectName("NButton")
        self.JButton = QtWidgets.QPushButton(self.frame)
        self.JButton.setGeometry(QtCore.QRect(420, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.JButton.setFont(font)
        self.JButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.JButton.setObjectName("JButton")
        self.LButton = QtWidgets.QPushButton(self.frame)
        self.LButton.setGeometry(QtCore.QRect(560, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.LButton.setFont(font)
        self.LButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.LButton.setObjectName("LButton")
        self.OButton = QtWidgets.QPushButton(self.frame)
        self.OButton.setGeometry(QtCore.QRect(560, 70, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.OButton.setFont(font)
        self.OButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.OButton.setObjectName("OButton")
        self.CButton = QtWidgets.QPushButton(self.frame)
        self.CButton.setGeometry(QtCore.QRect(140, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.CButton.setObjectName("CButton")
        self.Button_3 = QtWidgets.QPushButton(self.frame)
        self.Button_3.setGeometry(QtCore.QRect(140, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_3.setObjectName("Button_3")
        self.KButton = QtWidgets.QPushButton(self.frame)
        self.KButton.setGeometry(QtCore.QRect(490, 140, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.KButton.setFont(font)
        self.KButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.KButton.setObjectName("KButton")
        self.Button_dot = QtWidgets.QPushButton(self.frame)
        self.Button_dot.setGeometry(QtCore.QRect(700, 0, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Button_dot.setFont(font)
        self.Button_dot.setStyleSheet("border: 1px solid black;\n"
"border-radius: 3px;\n"
"color: #000947;\n"
"background-color: white;")
        self.Button_dot.setObjectName("Button_dot")
        self.plate_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.plate_1.setGeometry(QtCore.QRect(330, 280, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.plate_1.setFont(font)
        self.plate_1.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.plate_1.setFrame(True)
        self.plate_1.setAlignment(QtCore.Qt.AlignCenter)
        self.plate_1.setObjectName("plate_1")
        self.plate_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.plate_2.setGeometry(QtCore.QRect(450, 280, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.plate_2.setFont(font)
        self.plate_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.plate_2.setAlignment(QtCore.Qt.AlignCenter)
        self.plate_2.setObjectName("plate_2")
        self.plate_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.plate_3.setGeometry(QtCore.QRect(570, 280, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.plate_3.setFont(font)
        self.plate_3.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.plate_3.setAlignment(QtCore.Qt.AlignCenter)
        self.plate_3.setObjectName("plate_3")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(370, 110, 341, 71))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "plate.jpeg")))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(116, 192, 801, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")

        self.nextButton.setGeometry(QtCore.QRect(900, 600, 120, 120))
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.QButton.clicked.connect(lambda: self.key_press("Q"))
        self.WButton.clicked.connect(lambda: self.key_press("W"))
        self.EButton.clicked.connect(lambda: self.key_press("E"))
        self.RButton.clicked.connect(lambda: self.key_press("R"))
        self.TButton.clicked.connect(lambda: self.key_press("T"))
        self.YButton.clicked.connect(lambda: self.key_press("Y"))
        self.UButton.clicked.connect(lambda: self.key_press("U"))
        self.IButton.clicked.connect(lambda: self.key_press("I"))
        self.OButton.clicked.connect(lambda: self.key_press("O"))
        self.PButton.clicked.connect(lambda: self.key_press("P"))
        self.AButton.clicked.connect(lambda: self.key_press("A"))
        self.SButton.clicked.connect(lambda: self.key_press("S"))
        self.DButton.clicked.connect(lambda: self.key_press("D"))
        self.FButton.clicked.connect(lambda: self.key_press("F"))
        self.GButton.clicked.connect(lambda: self.key_press("G"))
        self.HButton.clicked.connect(lambda: self.key_press("H"))
        self.JButton.clicked.connect(lambda: self.key_press("J"))
        self.KButton.clicked.connect(lambda: self.key_press("K"))
        self.LButton.clicked.connect(lambda: self.key_press("L"))
        self.ZButton.clicked.connect(lambda: self.key_press("Z"))
        self.XButton.clicked.connect(lambda: self.key_press("X"))
        self.CButton.clicked.connect(lambda: self.key_press("C"))
        self.VButton.clicked.connect(lambda: self.key_press("V"))
        self.BButton.clicked.connect(lambda: self.key_press("B"))
        self.NButton.clicked.connect(lambda: self.key_press("N"))
        self.MButton.clicked.connect(lambda: self.key_press("M"))
        self.ButtonGerA.clicked.connect(lambda: self.key_press("Ä"))
        self.ButtonGerO.clicked.connect(lambda: self.key_press("Ö"))
        self.ButtonGerU.clicked.connect(lambda: self.key_press("Ü"))
        self.Button_1.clicked.connect(lambda: self.key_press("1"))
        self.Button_2.clicked.connect(lambda: self.key_press("2"))
        self.Button_3.clicked.connect(lambda: self.key_press("3"))
        self.Button_4.clicked.connect(lambda: self.key_press("4"))
        self.Button_5.clicked.connect(lambda: self.key_press("5"))
        self.Button_6.clicked.connect(lambda: self.key_press("6"))
        self.Button_7.clicked.connect(lambda: self.key_press("7"))
        self.Button_8.clicked.connect(lambda: self.key_press("8"))
        self.Button_9.clicked.connect(lambda: self.key_press("9"))
        self.Button_0.clicked.connect(lambda: self.key_press("0"))
        self.backButton_2.clicked.connect(lambda: self.key_press("<-"))

        self.Button_1.setFocusPolicy(Qt.NoFocus)
        self.Button_2.setFocusPolicy(Qt.NoFocus)
        self.Button_3.setFocusPolicy(Qt.NoFocus)
        self.Button_4.setFocusPolicy(Qt.NoFocus)
        self.Button_5.setFocusPolicy(Qt.NoFocus)
        self.Button_6.setFocusPolicy(Qt.NoFocus)
        self.Button_7.setFocusPolicy(Qt.NoFocus)
        self.Button_8.setFocusPolicy(Qt.NoFocus)
        self.Button_9.setFocusPolicy(Qt.NoFocus)
        self.Button_0.setFocusPolicy(Qt.NoFocus)
        self.backButton_2.setFocusPolicy(Qt.NoFocus)
        self.ButtonGerA.setFocusPolicy(Qt.NoFocus)
        self.ButtonGerO.setFocusPolicy(Qt.NoFocus)
        self.ButtonGerU.setFocusPolicy(Qt.NoFocus)
        self.QButton.setFocusPolicy(Qt.NoFocus)
        self.WButton.setFocusPolicy(Qt.NoFocus)
        self.EButton.setFocusPolicy(Qt.NoFocus)
        self.RButton.setFocusPolicy(Qt.NoFocus)
        self.TButton.setFocusPolicy(Qt.NoFocus)
        self.YButton.setFocusPolicy(Qt.NoFocus)
        self.UButton.setFocusPolicy(Qt.NoFocus)
        self.IButton.setFocusPolicy(Qt.NoFocus)
        self.OButton.setFocusPolicy(Qt.NoFocus)
        self.PButton.setFocusPolicy(Qt.NoFocus)
        self.AButton.setFocusPolicy(Qt.NoFocus)
        self.SButton.setFocusPolicy(Qt.NoFocus)
        self.DButton.setFocusPolicy(Qt.NoFocus)
        self.FButton.setFocusPolicy(Qt.NoFocus)
        self.GButton.setFocusPolicy(Qt.NoFocus)
        self.HButton.setFocusPolicy(Qt.NoFocus)
        self.JButton.setFocusPolicy(Qt.NoFocus)
        self.KButton.setFocusPolicy(Qt.NoFocus)
        self.LButton.setFocusPolicy(Qt.NoFocus)
        self.ZButton.setFocusPolicy(Qt.NoFocus)
        self.XButton.setFocusPolicy(Qt.NoFocus)
        self.CButton.setFocusPolicy(Qt.NoFocus)
        self.VButton.setFocusPolicy(Qt.NoFocus)
        self.BButton.setFocusPolicy(Qt.NoFocus)
        self.NButton.setFocusPolicy(Qt.NoFocus)
        self.MButton.setFocusPolicy(Qt.NoFocus)
        self.Button_dot.setFocusPolicy(Qt.NoFocus)

        self.homeButton.clicked.connect(self.gotohome)
        self.backButton.clicked.connect(self.back)
        self.nextButton.clicked.connect(self.next)

        if BaseLayout.PLATEC != "N":
            if BaseLayout.firstweight_data["vehicle"] == "":
                self.plate_1.setText("")
                self.plate_2.setText("")
                self.plate_3.setText("")
            else:
                plt = BaseLayout.firstweight_data["vehicle"].split(" ")
                if len(plt) >= 3:
                    self.plate_1.setText(plt[0])
                    self.plate_2.setText(plt[1])
                    self.plate_3.setText(plt[2])
                else:
                    self.plate_1.setText("")
                    self.plate_2.setText("")
                    self.plate_3.setText("")

    def retranslateUi(self, language):
        _translate = QtCore.QCoreApplication.translate
        language.setWindowTitle(_translate("language", "MainWindow"))
        self.PButton.setText(_translate("language", "P"))
        self.Button_5.setText(_translate("language", "5"))
        self.ButtonGerO.setText(_translate("language", "Ö"))
        self.GButton.setText(_translate("language", "G"))
        self.Button_7.setText(_translate("language", "7"))
        self.YButton.setText(_translate("language", "Y"))
        self.TButton.setText(_translate("language", "T"))
        self.WButton.setText(_translate("language", "W"))
        self.UButton.setText(_translate("language", "U"))
        self.XButton.setText(_translate("language", "X"))
        self.QButton.setText(_translate("language", "Q"))
        self.BButton.setText(_translate("language", "B"))
        self.DButton.setText(_translate("language", "D"))
        self.IButton.setText(_translate("language", "I"))
        self.Button_9.setText(_translate("language", "9"))
        self.backButton_2.setText(_translate("language", "<---------------"))
        self.VButton.setText(_translate("language", "V"))
        self.ZButton.setText(_translate("language", "Z"))
        self.ButtonGerA.setText(_translate("language", "Ä"))
        self.AButton.setText(_translate("language", "A"))
        self.Button_6.setText(_translate("language", "6"))
        self.RButton.setText(_translate("language", "R"))
        self.HButton.setText(_translate("language", "H"))
        self.Button_2.setText(_translate("language", "2"))
        self.Button_1.setText(_translate("language", "1"))
        self.MButton.setText(_translate("language", "M"))
        self.Button_0.setText(_translate("language", "0"))
        self.ButtonGerU.setText(_translate("language", "Ü"))
        self.FButton.setText(_translate("language", "F"))
        self.EButton.setText(_translate("language", "E"))
        self.SButton.setText(_translate("language", "S"))
        self.Button_4.setText(_translate("language", "4"))
        self.Button_8.setText(_translate("language", "8"))
        self.NButton.setText(_translate("language", "N"))
        self.JButton.setText(_translate("language", "J"))
        self.LButton.setText(_translate("language", "L"))
        self.OButton.setText(_translate("language", "O"))
        self.CButton.setText(_translate("language", "C"))
        self.Button_3.setText(_translate("language", "3"))
        self.KButton.setText(_translate("language", "K"))
        self.Button_dot.setText(_translate("language", "."))
        self.heading.setText(_translate("language", contstants.LANGUAGE_STORE[BaseLayout.lang]["check_extracted_license_plate"]))

    def key_press(self, text):
        if self.plate_1.hasFocus():
            if text not in "0123456789":
                if text == "<-":
                    txt = self.plate_1.text()
                    self.plate_1.setText(txt[:-1])
                else:
                    if len(self.plate_1.text()) < 3:
                        txt = self.plate_1.text()
                        txt += text
                        self.plate_1.setText(txt)
        elif self.plate_2.hasFocus():
            if text == "<-":
                txt = self.plate_2.text()
                self.plate_2.setText(txt[:-1])
            else:
                if len(self.plate_2.text()) < 3:
                    txt = self.plate_2.text()
                    txt += text
                    self.plate_2.setText(txt)
        elif self.plate_3.hasFocus():
            if text == "<-":
                txt = self.plate_3.text()
                self.plate_3.setText(txt[:-1])
            else:
                if len(self.plate_3.text()) < 4:
                    txt = self.plate_3.text()
                    txt += text
                    self.plate_3.setText(txt)


    def gotohome(self):
        if BaseLayout.thisWINDOW == self:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language.Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            return
    
    def back(self):
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(BarcodeScan.BarcodeScan())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()
        return

    def next(self):
        if len(self.plate_1.text()) > 0 and len(self.plate_2.text()) > 0 and len(self.plate_3.text()) > 0:
            BaseLayout.firstweight_data["vehicle"] = self.plate_1.text() + " " + self.plate_2.text() + " " + self.plate_3.text()
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(LicenseWait())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            if len(self.plate_1.text()) == 0:
                self.plate_1.setStyleSheet("background-color: rgb(212, 212, 212);\n"
                                        "border: 1px solid red;")
            if len(self.plate_2.text()) == 0:
                self.plate_2.setStyleSheet("background-color: rgb(212, 212, 212);\n"
                                        "border: 1px solid red;")
            if len(self.plate_3.text()) == 0:
                self.plate_3.setStyleSheet("background-color: rgb(212, 212, 212);\n"
                                        "border: 1px solid red;")
        return


class LicenseWait(BaseLayout.BaseLayout):
    def __init__(self):
        super(LicenseWait, self).__init__()
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
                    BaseLayout.widget.addWidget(Weighing.WeighingWait())
                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            except Exception as e:
                print(e)
                BaseLayout.widget.removeWidget(self)
                BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        else:
            try:
                vehicle_in_yard = check_vehicle(BaseLayout.firstweight_data["vehicle"])
                if vehicle_in_yard:
                    BaseLayout.widget.removeWidget(self)
                    BaseLayout.widget.addWidget(DisplayError.DisplayText(contstants.LANGUAGE_STORE[BaseLayout.lang]["already_in_list"], BarcodeScan.BarcodeScan()))
                    BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    return
                else:
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
                            BaseLayout.widget.addWidget(Weighing.WeighingWait())
                        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    except Exception as e:
                        print(e)
                        BaseLayout.widget.removeWidget(self)
                        BaseLayout.widget.addWidget(ConnectionError.ConnectionError())
                        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                    
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



class ExtractingLicense(BaseLayout.BaseLayout):
    def __init__(self):
        super(ExtractingLicense, self).__init__()
        self.setupUi()
        QtCore.QTimer.singleShot(1000, lambda: self.getData())

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 600)
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
        try:
            res = requests.get(url=BaseLayout.BASE_URL+f"/api/Vehicle-View/", headers=BaseLayout.get_headers, timeout=15).json()
            VEHICLE_LIST = res
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(LicenseList(VEHICLE_LIST))
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
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



class LicenseList(BaseLayout.BaseLayout):
    def __init__(self, mList):
        self.mList = mList
        super(LicenseList, self).__init__()       
        self.setupUi()
        BaseLayout.thisWINDOW = self
        QtCore.QTimer.singleShot(1000, lambda: self.focus())
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())

    def focus(self):
        self.textEdit.setFocus(True)
        return

    def setupUi(self):
        self.nameList = [(item["id"], item["license_plate"]) for item in self.mList]
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color:#fff;")
        self.centralwidget = HeadTemplate()
        self.centralwidget.setStyleSheet("QPushButton{\n"
                                         "background-color:#000947;\n"
                                         "color:#fff;\n"
                                         "font: 16pt \"Arial\";\n"
                                         "border-radius:15px\n"
                                         "}")
        self.screen_buttons(self.centralwidget)

        self.dataFrame = QtWidgets.QFrame(self.centralwidget)
        self.dataFrame.setGeometry(QtCore.QRect(20, 200, 981, 241))
        self.dataFrame.setStyleSheet("border:1px solid;\n"
                                     "border-radius:15px;font: 14pt \"Arial\"")
        self.dataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataFrame.setObjectName("dataFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.dataFrame)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 440, 761, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("QPushButton{"
                                 "border: 1px solid black;\n"
                                 "border-radius: 3px;\n"
                                 "color: #000947;\n"
                                 "background-color: white;}"
                                 )
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 160, 761, 51))
        self.textEdit.setStyleSheet("border:1px solid;\n"
                                    "border-radius:15px;font: 16pt \"Arial\";padding:4px")
        self.textEdit.setObjectName("textEdit")

        self.add_new_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_button.setGeometry(QtCore.QRect(825, 155, 171, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_new_button.sizePolicy().hasHeightForWidth())
        self.add_new_button.setSizePolicy(sizePolicy)
        self.add_new_button.setMinimumSize(QtCore.QSize(0, 50))
        self.add_new_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_new_button.setObjectName("add_new_button")
        self.keyboard_ui()
        self.setCentralWidget(self.centralwidget)
        self.buttonList = dict()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.backButton.setGeometry(QtCore.QRect(10, 630, 111, 111))
        self.backButton.setIconSize(QtCore.QSize(100, 100))
        self.backButton.setStyleSheet("background-color:#fff;border:none;")
        self.homeButton.setStyleSheet("background-color:#fff;border:none;")
        self.nextButton.hide()
        self.backButton.hide()
        
        self.add_new_button.clicked.connect(self.addnew)
        self.homeButton.clicked.connect(self.gotohome)


    def pressed(self, button):
        BaseLayout.firstweight_data["vehicle"] = str(
            button.name
        )
        BaseLayout.firstweight_data["VEHICLE_ID"] = str(
            button.id
        )
        
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(LicenseWait())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)           

        self.buttonList = {}
    
    def keyPressEvent(self, keyEvent): 
        return self.key_press("None")
            
            
    def key_press(self, text):
        
        for i, button in self.buttonList.items():
            button.button.close()
        
        if text == "<-":
            txt = self.textEdit.text()[:-1]
            self.textEdit.setText(txt)
        elif text == "None":
            txt = self.textEdit.text()
            txt = txt.upper()
        else:
            txt = self.textEdit.text()
            txt += text
            self.textEdit.setText(txt)

       
        nameList = []
        for name in self.nameList:
            if txt.upper() in name[1].upper():
                nameList.append(name)
            
        if len(nameList) == 0:
            self.add_new_button.show()
        else:
            for i in nameList:
                if str(txt) == str(i[1]).upper():
                  
                    self.add_new_button.hide()
                else:
                  
                    self.add_new_button.show()
        
        if self.textEdit.text() == "":
            nameList = []
        l = len(nameList)
        if l > 4:
            l = 4
        flag = 0
        for i in range(l):
            n = nameList[i]
            self.updateButton(i, n)

    def updateButton(self, i, n):
        self.suggestButton = QtWidgets.QPushButton(self.dataFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.suggestButton.sizePolicy().hasHeightForWidth())
        self.suggestButton.setSizePolicy(sizePolicy)
        self.suggestButton.setMinimumSize(QtCore.QSize(0, 50))
        self.suggestButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.suggestButton.setObjectName("suggestButton")
        self.suggestButton.setText(n[1])
        thisButton = BaseLayout.ButtonData(self.suggestButton, n[0], n[1], i)
        self.suggestButton.clicked.connect(lambda: self.pressed(thisButton))
        self.buttonList[i] = thisButton
        self.gridLayout.addWidget(self.suggestButton, i, 0, 1, 1)


    def addnew(self):
        txt = self.textEdit.text()
        if len(txt) > 0:
            BaseLayout.firstweight_data["vehicle"] = str(txt)
            BaseLayout.firstweight_data["VEHICLE_ID"] = None
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(LicenseWait())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()

        else:
            self.textEdit.setStyleSheet("border:1px solid red;\n"
                                "border-radius:15px;font: 16pt \"Arial\";padding:4px")

            
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["vehicle"]))
        self.add_new_button.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["add_new"]))
        keys.keyboard_labels(self, _translate)

    def gotohome(self):
        if BaseLayout.thisWINDOW == self:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language.Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            return