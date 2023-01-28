from time import time
from PyQt5 import QtWidgets, QtCore, QtGui
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language, License, ThankYou, ConnectionError, Signature, BarcodeScan
from src import contstants
from src.components.GetData import send_first_weight, send_second_weight, save_vehicle_weight, send_tara_weight



class WeightPanel(BaseLayout.BaseLayout):
    def __init__(self):
        super(WeightPanel, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())

    def setupUi(self):
        self.setObjectName("WeightPanel")
        self.resize(1024, 768)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()
        self.screen_buttons(self.centralwidget)

        self.msg_label = QtWidgets.QLabel(self.centralwidget)
        self.msg_label.setGeometry(QtCore.QRect(360, 150, 311, 61))
        self.msg_label.setStyleSheet(
            "border-bottom:2px solid #000947;\n"
            "color:#000947;\n"
            "font: 28pt \"Arial\";\n"
            "padding:0px;\n"
            "font-weight:bold;\n"
            "border-radius:15px"
        )
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")

        self.msg_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.msg_label_2.setGeometry(QtCore.QRect(10, 300, 951, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.msg_label_2.setFont(font)
        self.msg_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.msg_label_2.setAutoFillBackground(False)
        self.msg_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label_2.setObjectName("msg_label_2")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.homeButton.clicked.connect(self.gotohome)
        self.nextButton.clicked.connect(self.next)
        self.backButton.clicked.connect(self.back)

        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Weight", "WeightPanel"))
        if BaseLayout.weight_type == "first":
            self.msg_label.setText(_translate("Weight", contstants.LANGUAGE_STORE[BaseLayout.lang]["first_weight"]))
        elif BaseLayout.weight_type == "second":
            self.msg_label.setText(_translate("Weight", contstants.LANGUAGE_STORE[BaseLayout.lang]["second_weight"]))
        elif BaseLayout.weight_type == "tara_save":
            self.msg_label.setText(_translate("Weight", contstants.LANGUAGE_STORE[BaseLayout.lang]["tara_weight"]))
        elif BaseLayout.weight_type == "tara":
            self.msg_label.setText(_translate("Weight", contstants.LANGUAGE_STORE[BaseLayout.lang]["gross_weight"]))
        self.msg_label_2.setText(_translate("Weight", BaseLayout.weight + " kg"))
        
    def gotohome(self):
        if BaseLayout.thisWINDOW == self:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language.Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()
        else:
            return

    def next(self):
        if BaseLayout.weight_type == "first" or BaseLayout.weight_type == "tara_save":
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(WeighingWait())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        elif BaseLayout.weight_type == "second" or BaseLayout.weight_type == "tara":
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Signature.Signature())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()

    def back(self):
        if BaseLayout.weight_type == "first":
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(License.ConfirmLicense())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        elif BaseLayout.weight_type == "second" or BaseLayout.weight_type == "tara":
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(BarcodeScan.BarcodeScan())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        elif BaseLayout.weight_type == "tara_save":
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(License.ExtractingLicense())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()




class WeighingWait(BaseLayout.BaseLayout):
    def __init__(self):
        super(WeighingWait, self).__init__()
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
        res = False
        try:
            if BaseLayout.weight_type == "first":
                res = send_first_weight()
            elif BaseLayout.weight_type == "second":
                res = send_second_weight()
            elif BaseLayout.weight_type == "tara_save":
                res = save_vehicle_weight()
            elif BaseLayout.weight_type == "tara":
                res = send_tara_weight()
            if res:
                BaseLayout.widget.removeWidget(self)
                BaseLayout.widget.addWidget(ThankYou.ThankYou())
                BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
                return
            else:
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