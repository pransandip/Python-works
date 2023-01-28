from PyQt5 import QtWidgets, QtCore, QtGui
from src import contstants
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language, BarcodeScan
import os 




class DisplayText(BaseLayout.BaseLayout):
    def __init__(self, showText):
        self.showText = showText
        super(DisplayText, self).__init__()
        self.setupUi()
        self.next_timer = QtCore.QTimer()
        self.next_timer.timeout.connect(lambda: self.exit())
        self.next_timer.setSingleShot(True)
        self.next_timer.start(6000)

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color:#fff;")
        self.centralwidget = HeadTemplate()
        self.retry = QtWidgets.QLabel(self.centralwidget)
        self.retry.setGeometry(QtCore.QRect(260, 160, 555, 121))
        self.retry.setStyleSheet(
            "background-color:#DD4A4A;\n"
            "color:#fff;\n"
            'font: 28pt "Arial";\n'
            "border-radius:15px"
        )
        self.retry.setAlignment(QtCore.Qt.AlignCenter)
        self.retry.setObjectName("retry")
        self.showTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.showTextLabel.setGeometry(QtCore.QRect(0, 410, 1021, 91))
        self.showTextLabel.setStyleSheet('font: 17pt "Arial";')
        self.showTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showTextLabel.setObjectName("showTextLabel")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.retry.setText(_translate(
            "MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["retry_butt"]))
        self.showTextLabel.setText(
            _translate("MainWindow", self.showText)
        )

    def exit(self):
        self.next_timer.stop()
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(BarcodeScan.BarcodeScan())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()
        return