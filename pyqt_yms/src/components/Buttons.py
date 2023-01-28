from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QPushButton
from src import contstants
import os, gc

class LanguageButton(QPushButton):
    def __init__(self, parent, pos: tuple, location: str, name: str):
        super(LanguageButton, self).__init__(parent=parent)
        self.setGeometry(QtCore.QRect(*pos))
        self.setStyleSheet("border: none;\n" "")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(os.path.join(contstants.LANGUAGE_FLAG_IMAGES, location)), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(200, 130))
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setAutoRepeatDelay(200)
        self.setAutoRepeatInterval(101)
        self.setDefault(True)
        self.setObjectName(name)
        del icon 
        gc.collect()


class NextButton(QPushButton):
    def __init__(self, parent):
        super(NextButton, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QtCore.QRect(880, 580, 120, 120))
        self.setStyleSheet("border: none;background-color:#fff;")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "NextArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(120, 120))
        self.setObjectName("nextButton")


class BackButton(QPushButton):
    def __init__(self, parent):
        super(BackButton, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QtCore.QRect(0, 580, 120, 120))
        self.setStyleSheet("border: none;background-color:#fff;")
        self.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "BackArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.setIcon(icon1)
        self.setIconSize(QtCore.QSize(120, 120))
        self.setObjectName("backButton")


class HomeButton(QPushButton):
    def __init__(self, parent):
        super(HomeButton, self).__init__(parent=parent)
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QtCore.QRect(10, 20, 161, 131))
        self.setStyleSheet("border: none;background-color:#fff;")
        self.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "Home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.setIcon(icon7)
        self.setIconSize(QtCore.QSize(200, 200))
        self.setObjectName("homeButton")
