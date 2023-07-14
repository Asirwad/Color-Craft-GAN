import sys
import tensorflow as tf
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt, QFile, QTextStream

from app.ui.components.backgroundwidget import BackgroundWidget


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Color Craft GAN")
        self.setGeometry(200, 200, 1400, 800)
        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setFixedSize(self.size())
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # main window layout
        main_layout = QHBoxLayout()

        # Create the main content area
        self.main_content = BackgroundWidget()
        self.main_content.setObjectName("main_content")
        self.main_content.set_background_image('assets/component_bg/main_window_bg.png')
        self.main_layout = QVBoxLayout()
        self.main_content.setLayout(self.main_layout)

        # Add the side navigation and main content to the main window layout
        main_layout.addWidget(self.main_content)

        # Set the main window layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Add buttons to the main layout
        browse_grey_but = QPushButton("Browse grey-scale image", self)
        browse_grey_but.setObjectName("browse_grey_but")
        browse_grey_but.setGeometry(177, 646, 222, 47)  # Set position and size in pixels

        colorize_but = QPushButton("Colorize image", self)
        colorize_but.setObjectName("colorize_but")
        colorize_but.setGeometry(422, 646, 223, 47)  # Set position and size in pixels

    def load_stylesheet(self):
        styleshet = QFile("Styles/style.qss")
        if styleshet.open(QFile.ReadOnly | QFile.Text):
            print("hello")
            stream = QTextStream(styleshet)
            self.setStyleSheet(stream.readAll())


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
app = QApplication(sys.argv)
window = MainAppWindow()
window.load_stylesheet()
window.show()
sys.exit(app.exec_())
