from PyQt5 import QtWidgets,QtGui,QtCore
from src import contstants
import os 
class HeadTemplate(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.head_template()
        self.setStyleSheet("")
        self.setObjectName("centralwidget")

    def head_template(self):
        self.label_logo = QtWidgets.QLabel(self)
        self.label_logo.setGeometry(QtCore.QRect(790, 10, 181, 91))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "Logo.png")))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")