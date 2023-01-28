from time import time
from PyQt5 import QtWidgets, QtCore, QtGui
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language
from src import contstants
from src.components.GetData import green_on
import _thread

class ThankYou(QtWidgets.QMainWindow):
    def __init__(self):
        super(ThankYou, self).__init__()
        self.setupUi()
        QtCore.QTimer.singleShot(BaseLayout.LAST_PAGE_TIME, lambda: self.gotohome())

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet(
            "background-color:#fff;\n" 'font: 28pt "Arial";')
        self.centralwidget = HeadTemplate()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 230, 381, 111))
        self.label.setStyleSheet(
            "background-color:#000947;\n"
            "color:#fff;\n"
            'font: 28pt "Arial";\n'
            "border-radius:15px"
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 360, 1021, 81))
        self.label_2.setStyleSheet('font: 16pt "Arial";')
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        

    def gotohome(self):
        BaseLayout.RED = False
        _thread.start_new_thread(green_on, (None,))
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(Language.Language())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["thank_you"]))
        if BaseLayout.weight_type == "first":
            self.label_2.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["first_wight_thanks"]))
        elif BaseLayout.weight_type == "second" or BaseLayout.weight_type == "tara":
            self.label_2.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["wish_you_a_good_ride"]))
        elif BaseLayout.weight_type == "tara_save":
            self.label_2.setText(_translate("MainWindow", contstants.LANGUAGE_STORE[BaseLayout.lang]["tara_save"]))
