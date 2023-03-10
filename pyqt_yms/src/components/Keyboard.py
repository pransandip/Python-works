from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt


def keyboard(window):
    window.ButtonSpace = QtWidgets.QPushButton(window.frame)
    window.ButtonSpace.setGeometry(QtCore.QRect(630, 210, 131, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.ButtonSpace.setFont(font)

    window.ButtonSpace.setObjectName("ButtonSpace")
    window.PButton = QtWidgets.QPushButton(window.frame)
    window.PButton.setGeometry(QtCore.QRect(630, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.PButton.setFont(font)

    window.PButton.setObjectName("PButton")
    window.minusButton = QtWidgets.QPushButton(window.frame)
    window.minusButton.setGeometry(QtCore.QRect(700, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.minusButton.setFont(font)

    window.minusButton.setObjectName("minusButton")
    window.Button_5 = QtWidgets.QPushButton(window.frame)
    window.Button_5.setGeometry(QtCore.QRect(280, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_5.setFont(font)

    window.Button_5.setObjectName("Button_5")
    window.ButtonGerO = QtWidgets.QPushButton(window.frame)
    window.ButtonGerO.setGeometry(QtCore.QRect(700, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.ButtonGerO.setFont(font)

    window.ButtonGerO.setObjectName("ButtonGerO")
    window.GButton = QtWidgets.QPushButton(window.frame)
    window.GButton.setGeometry(QtCore.QRect(280, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.GButton.setFont(font)

    window.GButton.setObjectName("GButton")
    window.Button_7 = QtWidgets.QPushButton(window.frame)
    window.Button_7.setGeometry(QtCore.QRect(420, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_7.setFont(font)

    window.Button_7.setObjectName("Button_7")
    window.YButton = QtWidgets.QPushButton(window.frame)
    window.YButton.setGeometry(QtCore.QRect(350, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.YButton.setFont(font)

    window.YButton.setObjectName("YButton")
    window.TButton = QtWidgets.QPushButton(window.frame)
    window.TButton.setGeometry(QtCore.QRect(280, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.TButton.setFont(font)

    window.TButton.setObjectName("TButton")
    window.WButton = QtWidgets.QPushButton(window.frame)
    window.WButton.setGeometry(QtCore.QRect(70, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.WButton.setFont(font)

    window.WButton.setObjectName("WButton")
    window.UButton = QtWidgets.QPushButton(window.frame)
    window.UButton.setGeometry(QtCore.QRect(420, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.UButton.setFont(font)

    window.UButton.setObjectName("UButton")
    window.XButton = QtWidgets.QPushButton(window.frame)
    window.XButton.setGeometry(QtCore.QRect(70, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.XButton.setFont(font)

    window.XButton.setObjectName("XButton")
    window.QButton = QtWidgets.QPushButton(window.frame)
    window.QButton.setGeometry(QtCore.QRect(0, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.QButton.setFont(font)

    window.QButton.setObjectName("QButton")
    window.BButton = QtWidgets.QPushButton(window.frame)
    window.BButton.setGeometry(QtCore.QRect(280, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.BButton.setFont(font)

    window.BButton.setObjectName("BButton")
    window.DButton = QtWidgets.QPushButton(window.frame)
    window.DButton.setGeometry(QtCore.QRect(140, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.DButton.setFont(font)

    window.DButton.setObjectName("DButton")
    window.IButton = QtWidgets.QPushButton(window.frame)
    window.IButton.setGeometry(QtCore.QRect(490, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.IButton.setFont(font)

    window.IButton.setObjectName("IButton")
    window.Button_9 = QtWidgets.QPushButton(window.frame)
    window.Button_9.setGeometry(QtCore.QRect(560, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_9.setFont(font)

    window.Button_9.setObjectName("Button_9")
    window.backButton_2 = QtWidgets.QPushButton(window.frame)
    window.backButton_2.setGeometry(QtCore.QRect(700, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.backButton_2.setFont(font)
    window.backButton_2.setObjectName("backButton_2")
    window.VButton = QtWidgets.QPushButton(window.frame)
    window.VButton.setGeometry(QtCore.QRect(210, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.VButton.setFont(font)

    window.VButton.setObjectName("VButton")
    window.ZButton = QtWidgets.QPushButton(window.frame)
    window.ZButton.setGeometry(QtCore.QRect(0, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.ZButton.setFont(font)

    window.ZButton.setObjectName("ZButton")
    window.ButtonGerA = QtWidgets.QPushButton(window.frame)
    window.ButtonGerA.setGeometry(QtCore.QRect(630, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.ButtonGerA.setFont(font)

    window.ButtonGerA.setObjectName("ButtonGerA")
    window.AButton = QtWidgets.QPushButton(window.frame)
    window.AButton.setGeometry(QtCore.QRect(0, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.AButton.setFont(font)

    window.AButton.setObjectName("AButton")
    window.Button_6 = QtWidgets.QPushButton(window.frame)
    window.Button_6.setGeometry(QtCore.QRect(350, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_6.setFont(font)

    window.Button_6.setObjectName("Button_6")
    window.RButton = QtWidgets.QPushButton(window.frame)
    window.RButton.setGeometry(QtCore.QRect(210, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.RButton.setFont(font)

    window.RButton.setObjectName("RButton")
    window.HButton = QtWidgets.QPushButton(window.frame)
    window.HButton.setGeometry(QtCore.QRect(350, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.HButton.setFont(font)

    window.HButton.setObjectName("HButton")
    window.Button_2 = QtWidgets.QPushButton(window.frame)
    window.Button_2.setGeometry(QtCore.QRect(70, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_2.setFont(font)
    window.Button_2.setObjectName("Button_2")
    window.Button_1 = QtWidgets.QPushButton(window.frame)
    window.Button_1.setGeometry(QtCore.QRect(0, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_1.setFont(font)
    window.Button_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    window.Button_1.setAutoDefault(False)
    window.Button_1.setObjectName("Button_1")
    window.MButton = QtWidgets.QPushButton(window.frame)
    window.MButton.setGeometry(QtCore.QRect(420, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.MButton.setFont(font)

    window.MButton.setObjectName("MButton")
    window.Button_0 = QtWidgets.QPushButton(window.frame)
    window.Button_0.setGeometry(QtCore.QRect(630, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_0.setFont(font)

    window.Button_0.setObjectName("Button_0")
    window.ButtonGerU = QtWidgets.QPushButton(window.frame)
    window.ButtonGerU.setGeometry(QtCore.QRect(490, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.ButtonGerU.setFont(font)

    window.ButtonGerU.setObjectName("ButtonGerU")
    window.FButton = QtWidgets.QPushButton(window.frame)
    window.FButton.setGeometry(QtCore.QRect(210, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.FButton.setFont(font)

    window.FButton.setObjectName("FButton")
    window.EButton = QtWidgets.QPushButton(window.frame)
    window.EButton.setGeometry(QtCore.QRect(140, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.EButton.setFont(font)

    window.EButton.setObjectName("EButton")
    window.SButton = QtWidgets.QPushButton(window.frame)
    window.SButton.setGeometry(QtCore.QRect(70, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.SButton.setFont(font)

    window.SButton.setObjectName("SButton")
    window.Button_4 = QtWidgets.QPushButton(window.frame)
    window.Button_4.setGeometry(QtCore.QRect(210, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_4.setFont(font)

    window.Button_4.setObjectName("Button_4")
    window.Button_8 = QtWidgets.QPushButton(window.frame)
    window.Button_8.setGeometry(QtCore.QRect(490, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_8.setFont(font)

    window.Button_8.setObjectName("Button_8")
    window.NButton = QtWidgets.QPushButton(window.frame)
    window.NButton.setGeometry(QtCore.QRect(350, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.NButton.setFont(font)

    window.NButton.setObjectName("NButton")
    window.JButton = QtWidgets.QPushButton(window.frame)
    window.JButton.setGeometry(QtCore.QRect(420, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.JButton.setFont(font)

    window.JButton.setObjectName("JButton")
    window.LButton = QtWidgets.QPushButton(window.frame)
    window.LButton.setGeometry(QtCore.QRect(560, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.LButton.setFont(font)

    window.LButton.setObjectName("LButton")
    window.OButton = QtWidgets.QPushButton(window.frame)
    window.OButton.setGeometry(QtCore.QRect(560, 70, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.OButton.setFont(font)

    window.OButton.setObjectName("OButton")
    window.CButton = QtWidgets.QPushButton(window.frame)
    window.CButton.setGeometry(QtCore.QRect(140, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.CButton.setFont(font)

    window.CButton.setObjectName("CButton")
    window.ButtonGerU_2 = QtWidgets.QPushButton(window.frame)
    window.ButtonGerU_2.setGeometry(QtCore.QRect(560, 210, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.ButtonGerU_2.setFont(font)
    window.ButtonGerU_2.setObjectName("ButtonGerU_2")
    window.Button_3 = QtWidgets.QPushButton(window.frame)
    window.Button_3.setGeometry(QtCore.QRect(140, 0, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.Button_3.setFont(font)
    window.Button_3.setObjectName("Button_3")
    window.KButton = QtWidgets.QPushButton(window.frame)
    window.KButton.setGeometry(QtCore.QRect(490, 140, 61, 61))
    font = QtGui.QFont()
    font.setPointSize(14)
    font.setBold(True)
    window.KButton.setFont(font)
    window.KButton.setObjectName("KButton")
    window.QButton.clicked.connect(lambda: window.key_press("Q"))
    window.WButton.clicked.connect(lambda: window.key_press("W"))
    window.EButton.clicked.connect(lambda: window.key_press("E"))
    window.RButton.clicked.connect(lambda: window.key_press("R"))
    window.TButton.clicked.connect(lambda: window.key_press("T"))
    window.YButton.clicked.connect(lambda: window.key_press("Z"))
    window.UButton.clicked.connect(lambda: window.key_press("U"))
    window.IButton.clicked.connect(lambda: window.key_press("I"))
    window.OButton.clicked.connect(lambda: window.key_press("O"))
    window.PButton.clicked.connect(lambda: window.key_press("P"))
    window.AButton.clicked.connect(lambda: window.key_press("A"))
    window.SButton.clicked.connect(lambda: window.key_press("S"))
    window.DButton.clicked.connect(lambda: window.key_press("D"))
    window.FButton.clicked.connect(lambda: window.key_press("F"))
    window.GButton.clicked.connect(lambda: window.key_press("G"))
    window.HButton.clicked.connect(lambda: window.key_press("H"))
    window.JButton.clicked.connect(lambda: window.key_press("J"))
    window.KButton.clicked.connect(lambda: window.key_press("K"))
    window.LButton.clicked.connect(lambda: window.key_press("L"))
    window.ZButton.clicked.connect(lambda: window.key_press("Y"))
    window.XButton.clicked.connect(lambda: window.key_press("X"))
    window.CButton.clicked.connect(lambda: window.key_press("C"))
    window.VButton.clicked.connect(lambda: window.key_press("V"))
    window.BButton.clicked.connect(lambda: window.key_press("B"))
    window.NButton.clicked.connect(lambda: window.key_press("N"))
    window.MButton.clicked.connect(lambda: window.key_press("M"))
    window.ButtonGerA.clicked.connect(lambda: window.key_press("??"))
    window.ButtonGerO.clicked.connect(lambda: window.key_press("??"))
    window.ButtonGerU.clicked.connect(lambda: window.key_press("??"))
    window.ButtonGerU_2.clicked.connect(lambda: window.key_press("."))
    window.Button_1.clicked.connect(lambda: window.key_press("1"))
    window.Button_2.clicked.connect(lambda: window.key_press("2"))
    window.Button_3.clicked.connect(lambda: window.key_press("3"))
    window.Button_4.clicked.connect(lambda: window.key_press("4"))
    window.Button_5.clicked.connect(lambda: window.key_press("5"))
    window.Button_6.clicked.connect(lambda: window.key_press("6"))
    window.Button_7.clicked.connect(lambda: window.key_press("7"))
    window.Button_8.clicked.connect(lambda: window.key_press("8"))
    window.Button_9.clicked.connect(lambda: window.key_press("9"))
    window.Button_0.clicked.connect(lambda: window.key_press("0"))
    window.minusButton.clicked.connect(lambda: window.key_press("-"))
    window.backButton_2.clicked.connect(lambda: window.key_press("<-"))
    window.ButtonSpace.clicked.connect(lambda: window.key_press(" "))

    window.Button_1.setFocusPolicy(Qt.NoFocus)
    window.Button_2.setFocusPolicy(Qt.NoFocus)
    window.Button_3.setFocusPolicy(Qt.NoFocus)
    window.Button_4.setFocusPolicy(Qt.NoFocus)
    window.Button_5.setFocusPolicy(Qt.NoFocus)
    window.Button_6.setFocusPolicy(Qt.NoFocus)
    window.Button_7.setFocusPolicy(Qt.NoFocus)
    window.Button_8.setFocusPolicy(Qt.NoFocus)
    window.Button_9.setFocusPolicy(Qt.NoFocus)
    window.Button_0.setFocusPolicy(Qt.NoFocus)
    window.minusButton.setFocusPolicy(Qt.NoFocus)
    window.backButton_2.setFocusPolicy(Qt.NoFocus)
    window.ButtonSpace.setFocusPolicy(Qt.NoFocus)
    window.ButtonGerA.setFocusPolicy(Qt.NoFocus)
    window.ButtonGerO.setFocusPolicy(Qt.NoFocus)
    window.ButtonGerU.setFocusPolicy(Qt.NoFocus)
    window.ButtonGerU_2.setFocusPolicy(Qt.NoFocus)
    window.QButton.setFocusPolicy(Qt.NoFocus)
    window.WButton.setFocusPolicy(Qt.NoFocus)
    window.EButton.setFocusPolicy(Qt.NoFocus)
    window.RButton.setFocusPolicy(Qt.NoFocus)
    window.TButton.setFocusPolicy(Qt.NoFocus)
    window.YButton.setFocusPolicy(Qt.NoFocus)
    window.UButton.setFocusPolicy(Qt.NoFocus)
    window.IButton.setFocusPolicy(Qt.NoFocus)
    window.OButton.setFocusPolicy(Qt.NoFocus)
    window.PButton.setFocusPolicy(Qt.NoFocus)
    window.AButton.setFocusPolicy(Qt.NoFocus)
    window.SButton.setFocusPolicy(Qt.NoFocus)
    window.DButton.setFocusPolicy(Qt.NoFocus)
    window.FButton.setFocusPolicy(Qt.NoFocus)
    window.GButton.setFocusPolicy(Qt.NoFocus)
    window.HButton.setFocusPolicy(Qt.NoFocus)
    window.JButton.setFocusPolicy(Qt.NoFocus)
    window.KButton.setFocusPolicy(Qt.NoFocus)
    window.LButton.setFocusPolicy(Qt.NoFocus)
    window.ZButton.setFocusPolicy(Qt.NoFocus)
    window.XButton.setFocusPolicy(Qt.NoFocus)
    window.CButton.setFocusPolicy(Qt.NoFocus)
    window.VButton.setFocusPolicy(Qt.NoFocus)
    window.BButton.setFocusPolicy(Qt.NoFocus)
    window.NButton.setFocusPolicy(Qt.NoFocus)
    window.MButton.setFocusPolicy(Qt.NoFocus)


def keyboard_labels(window, _translate):
    window.BButton.setText(_translate("licenseplate", "B"))
    window.FButton.setText(_translate("licenseplate", "F"))
    window.UButton.setText(_translate("licenseplate", "U"))
    window.KButton.setText(_translate("licenseplate", "K"))
    window.IButton.setText(_translate("licenseplate", "I"))
    window.PButton.setText(_translate("licenseplate", "P"))
    window.Button_7.setText(_translate("licenseplate", "7"))
    window.JButton.setText(_translate("licenseplate", "J"))
    window.YButton.setText(_translate("licenseplate", "Z"))
    window.EButton.setText(_translate("licenseplate", "E"))
    window.Button_1.setText(_translate("licenseplate", "1"))
    window.GButton.setText(_translate("licenseplate", "G"))
    window.WButton.setText(_translate("licenseplate", "W"))
    window.OButton.setText(_translate("licenseplate", "O"))
    window.XButton.setText(_translate("licenseplate", "X"))
    window.ButtonSpace.setText(_translate("licenseplate", "SPACE"))
    window.HButton.setText(_translate("licenseplate", "H"))
    window.Button_2.setText(_translate("licenseplate", "2"))
    window.RButton.setText(_translate("licenseplate", "R"))
    window.NButton.setText(_translate("licenseplate", "N"))
    window.MButton.setText(_translate("licenseplate", "M"))
    window.Button_4.setText(_translate("licenseplate", "4"))
    window.Button_5.setText(_translate("licenseplate", "5"))
    window.Button_0.setText(_translate("licenseplate", "0"))
    window.ButtonGerO.setText(_translate("licenseplate", "??"))
    window.ButtonGerU.setText(_translate("licenseplate", "??"))
    window.ZButton.setText(_translate("licenseplate", "Y"))
    window.VButton.setText(_translate("licenseplate", "V"))
    window.backButton_2.setText(_translate("licenseplate", "<-"))
    window.SButton.setText(_translate("licenseplate", "S"))
    window.QButton.setText(_translate("licenseplate", "Q"))
    window.Button_9.setText(_translate("licenseplate", "9"))
    window.TButton.setText(_translate("licenseplate", "T"))
    window.Button_8.setText(_translate("licenseplate", "8"))
    window.AButton.setText(_translate("licenseplate", "A"))
    window.Button_3.setText(_translate("licenseplate", "3"))
    window.DButton.setText(_translate("licenseplate", "D"))
    window.CButton.setText(_translate("licenseplate", "C"))
    window.ButtonGerA.setText(_translate("licenseplate", "??"))
    window.Button_6.setText(_translate("licenseplate", "6"))
    window.minusButton.setText(_translate("licenseplate", "-"))
    window.LButton.setText(_translate("licenseplate", "L"))
    window.ButtonGerU_2.setText(_translate("licenseplate", "."))