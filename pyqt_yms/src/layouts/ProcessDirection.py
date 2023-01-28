from time import time
from PyQt5 import QtWidgets, QtCore, QtGui
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language, License, ConnectionError, BarcodeScan, Weighing, Signature
from src import contstants


class ProcessDirection(BaseLayout.BaseLayout):
    def __init__(self):
        super(ProcessDirection, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())

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
        self.yesButton = QtWidgets.QPushButton(self.centralwidget)
        self.yesButton.setGeometry(QtCore.QRect(240, 360, 261, 91))
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(self.centralwidget)
        self.noButton.setGeometry(QtCore.QRect(520, 360, 261, 91))
        self.noButton.setObjectName("noButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 270, 561, 61))
        self.label.setStyleSheet("\n" 'font: 19pt "Arial";')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.nextButton.hide()
        self.yesButton.clicked.connect(lambda: self.process("0"))
        self.noButton.clicked.connect(lambda: self.process("1"))
        self.homeButton.clicked.connect(self.gotohome)
        self.backButton.clicked.connect(self.back)

    def process(self, status):
        BaseLayout.process_direction = status
        BaseLayout.widget.removeWidget(self)
        if BaseLayout.WEIGHT_SCREEN:
            BaseLayout.widget.addWidget(Weighing.WeightPanel())
        else:
            BaseLayout.widget.addWidget(Signature.Signature())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()

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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yesButton.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["input"]))
        self.noButton.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["output"]))
        self.label.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["status"]))