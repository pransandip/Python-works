from PyQt5 import QtWidgets, QtCore, QtGui
from src.components.HeadTemplate import HeadTemplate
from src.layouts import BaseLayout, ThankYou, Language, Weighing
from src import contstants
from PyQt5.QtCore import Qt
import base64

class Signature(BaseLayout.BaseLayout):
    def __init__(self):
        super(Signature, self).__init__()
        self.setupUi()
        BaseLayout.thisWINDOW = self
        QtCore.QTimer.singleShot(BaseLayout.WAIT_TIME * 60000, lambda: self.gotohome())

    def setupUi(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setObjectName("self")
        self.resize(1024, 768)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = HeadTemplate()
        self.screen_buttons(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 610, 171, 41))
        self.pushButton.setStyleSheet(
            "border: 1px solid black;\n"
            "font: bold 18px;\n"
            "font-family: Arial;\n"
            "color: #000947;\n"
            "background-color: white;"
        )
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 150, 600, 61))
        self.label.setStyleSheet(
            "border-bottom:2px solid #000947;\n"
            "color:#000947;\n"
            "font: 28pt \"Arial\";\n"
            "padding:0px;\n"
            "font-weight:bold;\n"
            "border-radius:15px"
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(139, 220, 721, 371))
        self.frame.setStyleSheet("border: 1px solid;background-color:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 12
        self.brushColor = Qt.black

        self.lastPoint = QtCore.QPoint()

        self.pushButton.clicked.connect(lambda: self.clear())
        # self.b_ok.clicked.connect(lambda: self.save())
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.moved = False

        self.nextButton.clicked.connect(self.save)
        self.backButton.clicked.connect(self.back)
        self.homeButton.clicked.connect(self.gotohome)

    def back(self):
        BaseLayout.widget.removeWidget(self)
        BaseLayout.widget.addWidget(Weighing.WeightPanel())
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

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("signature", "MainWindow"))
        self.label.setText(_translate("window", contstants.LANGUAGE_STORE[BaseLayout.lang]["signature"]))
        self.pushButton.setText(_translate("window", contstants.LANGUAGE_STORE[BaseLayout.lang]["reset"]))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.current = event.pos()

            if (
                self.current.x() > 139
                and self.current.y() > 221
                and self.current.x() < 859
                and self.current.y() < 589
            ):
                self.drawing = True
                self.lastPoint = event.pos()
            else:
                self.lastPoint = None

    def mouseMoveEvent(self, event):
        self.moved = True

        if (event.buttons() & Qt.LeftButton) & self.drawing:

            painter = QtGui.QPainter(self.image)

            painter.setPen(
                QtGui.QPen(
                    self.brushColor,
                    self.brushSize,
                    Qt.SolidLine,
                    Qt.RoundCap,
                    Qt.RoundJoin,
                )
            )
            self.current = event.pos()
            if (
                self.current.x() > 139
                and self.current.y() > 221
                and self.current.x() < 859
                and self.current.y() < 589
            ):
                painter.drawLine(self.lastPoint, event.pos())
                self.lastPoint = event.pos()
                self.update()

            # painter.drawPixmap(QRect(0, 0, pixmap.width(), pixmap.height()), pixmap)

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QtGui.QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        if self.moved:
            self.image.save("image.jpeg")
            
            with open("image.jpeg", "rb") as img_file:
                img_string = base64.b64encode(img_file.read()).decode("utf-8")
                BaseLayout.img_string = str(img_string)
            # os.remove("image.jpeg")

            BaseLayout.widget.removeWidget(self)
            BaseLayout.widget.addWidget(Weighing.WeighingWait())
            BaseLayout.widget.setCurrentIndex(BaseLayout.widget.currentIndex() + 1)
            self.deleteLater()

    def clear(self):
        self.image.fill(Qt.white)
        self.update()



