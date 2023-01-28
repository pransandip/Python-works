from PyQt5 import QtWidgets, QtCore, QtGui
from src import contstants
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, Language
import os, _thread, requests

nowRunning = False
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

class ConnectionError(BaseLayout.BaseLayout):
    def __init__(self):
        super(ConnectionError, self).__init__()
        self.setupUi()
        _thread.start_new_thread(check_connection_timelimit, (None,))
        QtCore.QTimer.singleShot(20000, lambda: self.get())

    def setupUi(self):
        self.setObjectName("licenseplate")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 270, 941, 241))
        self.label.setStyleSheet("font: bold 40px;\n"
"font-family: Arial;\n"
"color: #000947;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get(self):
        global nowRunning
        if nowRunning:
            nowRunning = False
            try:
                BaseLayout.thisWINDOW.getData()
            except:
                pass
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(BaseLayout.thisWINDOW)
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        else:
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Language())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()

    def retranslateUi(self, licenseplate):
        _translate = QtCore.QCoreApplication.translate
        licenseplate.setWindowTitle(_translate("licenseplate", "MainWindow"))
        #self.i18n = I18N(lang)
        self.label.setText(_translate("licenseplate", 'Trying to reconnect...'))