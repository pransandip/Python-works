from PyQt5 import QtWidgets, QtCore, QtGui
from src import contstants
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, EnterPin
from src.layouts.BarcodeScan import BarcodeScan
from src.components.Buttons import LanguageButton
from src.components.GetData import red_on, green_on, default_global
import os, _thread

class Language(BaseLayout.BaseLayout):
    def __init__(self):
        super(Language, self).__init__()
        self.setupUi()
        default_global()
        BaseLayout.thisWINDOW = self
        if BaseLayout.RED:
            BaseLayout.RED = False
            _thread.start_new_thread(green_on, (None,))

    def setupUi(self):
        self.setObjectName("language")
        self.resize(1024, 768)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()

        self.englishButton = LanguageButton(self.centralwidget, (40, 200, 170, 120),
                                            "GB.png", "englishButton")
        self.englishButton.clicked.connect(lambda: self.clicked("en"))

        self.germanButton = LanguageButton(self.centralwidget, (230, 200, 170, 120),
                                           "DE.png", "germanButton")
        self.germanButton.clicked.connect(lambda: self.clicked("de"))

        self.frenchButton = LanguageButton(self.centralwidget, (420, 200, 170, 120),
                                           "FR.png", "frenchButton")
        self.frenchButton.clicked.connect(lambda: self.clicked("fr"))

        self.romanianButton = LanguageButton(self.centralwidget, (610, 350, 170, 120),
                                             "RO.png", "romanianButton")
        self.romanianButton.clicked.connect(lambda: self.clicked("pl"))

        self.turkishButton = LanguageButton(self.centralwidget, (420, 500, 170, 120),
                                            "TR.png", "turkishButton")
        self.turkishButton.clicked.connect(lambda: self.clicked("ru"))

        self.polandButton = LanguageButton(self.centralwidget, (610, 200, 170, 120),
                                           "Poland.png", "polandButton")
        self.polandButton.clicked.connect(lambda: self.clicked("pl"))

        self.russiaButton = LanguageButton(self.centralwidget, (800, 200, 170, 120),
                                           "Russia.png", "russiaButton")
        self.russiaButton.clicked.connect(lambda: self.clicked("ru"))

        self.czechButton = LanguageButton(self.centralwidget, (40, 350, 170, 120),
                                          "Czech_Republic.png", "czechButton")
        self.czechButton.clicked.connect(lambda: self.clicked("cr"))

        self.croatiaButton = LanguageButton(self.centralwidget, (230, 350, 170, 120),
                                            "Croatia.png", "croatiaButton")
        self.croatiaButton.clicked.connect(lambda: self.clicked("cs"))

        self.hungaryButton = LanguageButton(self.centralwidget, (420, 350, 170, 120),
                                            "Hungary.png", "hungaryButton")
        self.hungaryButton.clicked.connect(lambda: self.clicked("hu"))

        self.bulgariaButton = LanguageButton(self.centralwidget, (800, 350, 170, 120),
                                             "Bulgaria.png", "bulgariaButton")
        self.bulgariaButton.clicked.connect(lambda: self.clicked("bg"))

        self.siberiaButton = LanguageButton(self.centralwidget, (230, 500, 170, 120),
                                             "Serbia.png", "siberiaButton")
        self.siberiaButton.clicked.connect(lambda: self.clicked("sr"))
        
        self.netherlandButton = LanguageButton(self.centralwidget, (610, 500, 170, 120),
                                             "Netherlands.png", "netherlandButton")
        self.netherlandButton.clicked.connect(lambda: self.clicked("nl"))


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 180, 971, 311))
        self.frame.setStyleSheet("background-color: #d9d9d9;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(210, 490, 591, 151))
        self.frame_2.setStyleSheet("background-color: #d9d9d9;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame.raise_()
        self.frame_2.raise_()

        self.englishButton.raise_()
        self.germanButton.raise_()
        self.frenchButton.raise_()
        self.romanianButton.raise_()
        self.turkishButton.raise_()
        self.polandButton.raise_()
        self.russiaButton.raise_()
        self.czechButton.raise_()
        self.croatiaButton.raise_()
        self.hungaryButton.raise_()
        self.bulgariaButton.raise_()
        self.siberiaButton.raise_()
        self.netherlandButton.raise_()
        self.label_logo = QtWidgets.QPushButton(self.centralwidget)
        self.label_logo.setGeometry(QtCore.QRect(790, 10, 181, 91))
        self.label_logo.setObjectName("label_logo")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(os.path.join(contstants.ASSETS_IMAGES, "Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.label_logo.setIcon(icon)
        self.label_logo.setIconSize(QtCore.QSize(181, 91))
        self.label_logo.setStyleSheet("border: none;background-color:#fff;")

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.label_logo.clicked.connect(self.admin)

        
    def retranslateUi(self, language):
        _translate = QtCore.QCoreApplication.translate
        language.setWindowTitle(_translate("language", "language"))

    def clicked(self, text):
        BaseLayout.lang = text
        _thread.start_new_thread(red_on, (None,))
        BaseLayout.RED = True
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(BarcodeScan())
        BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
        self.deleteLater()

    def admin(self):
        if BaseLayout.TARASAVE:
            _thread.start_new_thread(red_on, (None,))
            BaseLayout.RED = True
            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(EnterPin.EnterPin())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()

