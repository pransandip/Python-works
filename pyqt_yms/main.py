import sys, _thread
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from src.layouts.Language import Language
from src.layouts import BaseLayout
from src.components import GetData

if __name__ == "__main__":
    app = QApplication(sys.argv)
    BaseLayout.init()
    if not BaseLayout.OLD:
        GetData.get_token()
    start_window = Language()
    BaseLayout.widget.addWidget(start_window)
    BaseLayout.widget.setFixedHeight(768)
    BaseLayout.widget.setFixedWidth(1024)
    BaseLayout.widget.setWindowFlag(Qt.FramelessWindowHint)
    BaseLayout.widget.show()
    sys.exit(app.exec_())