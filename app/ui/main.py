import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLabel, \
    QSpacerItem, QSizePolicy, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QFile, QTextStream

from app.ui.components.backgroundwidget import BackgroundWidget


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # vars
        self.grey_image_label = None
        self.grey_image_filepath = None

        # window properties
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

        # Add the main content to the main window layout
        main_layout.addWidget(self.main_content)

        # Set the main window layout
        central_widget = QWidget()
        central_widget.setObjectName("central_widget")
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # grayscale image label
        grey_image_label = QLabel()
        pixmap = QPixmap("assets/image_dummies/grey_dummy.png")
        grey_image_label.setPixmap(pixmap.scaled(245, 245, Qt.KeepAspectRatio))
        grey_image_label.setGeometry(762, 152, 245, 245)

        # color image label
        color_image_label = QLabel("", self)
        pixmap = QPixmap("assets/image_dummies/color_dummy.png")
        color_image_label.setPixmap(pixmap.scaled(245, 245, Qt.KeepAspectRatio))
        color_image_label.setGeometry(762, 481, 245, 245)

        # Add buttons to the main layout
        browse_grey_but = QPushButton("Browse grey-scale image", self)
        browse_grey_but.setObjectName("browse_grey_but")
        browse_grey_but.setGeometry(177, 646, 222, 47)
        browse_grey_but.clicked.connect(self.browse_grayscale_image)

        colorize_but = QPushButton("Colorize image", self)
        colorize_but.setObjectName("colorize_but")
        colorize_but.setGeometry(422, 646, 223, 47)
        colorize_but.clicked.connect(self.colorize_image)

    def load_stylesheet(self):
        stylesheet = QFile("Styles/style.qss")
        if stylesheet.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(stylesheet)
            self.setStyleSheet(stream.readAll())

    def browse_grayscale_image(self):
        file_dialog = QFileDialog()
        self.grey_image_filepath, _ = file_dialog.getOpenFileName(self, "Select grey scale Image")
        if self.grey_image_filepath:
            pixmap = QPixmap(self.grey_image_filepath)
            self.grey_image_label.setPixmap(pixmap.scaled(245, 245, Qt.KeepAspectRatio))

    def colorize_image(self):
        # Placeholder function for colorizing the image using TensorFlow
        # You can perform the colorization process here using TensorFlow

        # Example code to display a message box
        QMessageBox.information(self, "Colorize Image", "Colorization process completed.")


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
app = QApplication(sys.argv)
window = MainAppWindow()
window.load_stylesheet()
window.show()
sys.exit(app.exec_())
