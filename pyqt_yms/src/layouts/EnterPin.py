from PyQt5 import QtWidgets, QtCore, QtGui
from src import contstants
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language, License, BarcodeScan
import datetime, _thread, os, time

class EnterPin(BaseLayout.BaseLayout):
    def __init__(self):
        super(EnterPin, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        BaseLayout.lang = "de"
        QtCore.QTimer.singleShot(10000, lambda: self.home())
    
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.setStyleSheet("background-color:#fff;")
        self.centralwidget = HeadTemplate()
        self.centralwidget.setStyleSheet(
            "QPushButton{\n"
            "background-color:#000947;\n"
            "color:#fff;\n"
            'font: 16pt "Arial";\n'
            "border-radius:15px\n"
            "}"
        )
        self.screen_buttons(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 140, 561, 61))
        self.label.setStyleSheet("\n"
"font: 19pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(280, 330, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_1.setFont(font)
        self.Button_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_1.setStyleSheet("")
        self.Button_1.setAutoDefault(False)
        self.Button_1.setObjectName("Button_1")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(400, 330, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_2.setFont(font)
        self.Button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_2.setStyleSheet("")
        self.Button_2.setObjectName("Button_2")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(280, 570, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("")
        self.Button_7.setObjectName("Button_7")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(400, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("")
        self.Button_5.setObjectName("Button_5")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(400, 570, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("")
        self.Button_8.setObjectName("Button_8")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(520, 570, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("")
        self.Button_9.setObjectName("Button_9")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(520, 330, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_3.setFont(font)
        self.Button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Button_3.setStyleSheet("")
        self.Button_3.setObjectName("Button_3")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(520, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("")
        self.Button_6.setObjectName("Button_6")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(280, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("")
        self.Button_4.setObjectName("Button_4")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(640, 450, 101, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("")
        self.Button_0.setObjectName("Button_0")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 210, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 16pt \"Arial\";\n"
"border-radius:15px;\n"
"border: 1px solid black;")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.Button_back = QtWidgets.QPushButton(self.centralwidget)
        self.Button_back.setGeometry(QtCore.QRect(640, 330, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Button_back.setFont(font)
        self.Button_back.setStyleSheet("")
        self.Button_back.setObjectName("Button_back")

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.homeButton.clicked.connect(self.home)
        self.nextButton.clicked.connect(self.next)
        self.backButton.hide()

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
        self.Button_back.clicked.connect(lambda: self.key_press("<-"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PIN-CODE EINGEBEN"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_back.setText(_translate("MainWindow", "<"))
    
    def home(self):
        if BaseLayout.thisWINDOW == self:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language.Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            return

    
    def next(self):
        if int(self.lineEdit.text()) == BaseLayout.PINCODE:
            BaseLayout.weight_type = "tara_save"
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(BarcodeScan.BarcodeScan())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            self.lineEdit.setStyleSheet("font: 16pt \"Arial\";\n"
                                        "border-radius:15px;\n"
                                        "border: 1px solid red;")


    def key_press(self, text):
        if text == "<-":
            txt = self.lineEdit.text()
            self.lineEdit.setText(txt[:-1])
        else:
            txt = self.lineEdit.text()
            txt += text
            self.lineEdit.setText(txt)