import sys
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QGridLayout, \
    QSpacerItem, QSizePolicy, QLabel
from PyQt5.QtCore import Qt, QFile, QTextStream
from app.ui.components.backgroundwidget import BackgroundWidget


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window properties
        self.setWindowIcon(QIcon("assets/icon.ico"))
        self.setGeometry(200, 200, 1400, 800)
        self.setFixedSize(self.size())
        self.setWindowTitle("Color Craft GAN")

        # set main layout
        main_layout = QHBoxLayout()

        # create the main content area
        self.main_content = BackgroundWidget()
        self.main_content.setObjectName("main_content")
        self.main_content.set_background_image("assets/component_bg/welcome_bg.png")
        self.main_content_layout = QGridLayout()
        self.main_content.setLayout(self.main_content_layout)

        main_layout.addWidget(self.main_content)

        # button
        continue_button = QPushButton("Colorise")
        continue_button.setObjectName("continue_button")
        continue_button.setFixedSize(220, 45)
        continue_button.clicked.connect(self.show_colorize_page)
        font = QFont("Arial", 15, QFont.Bold)
        continue_button.setFont(font)

        # Add the button to the layout with specific positioning and alignment
        self.main_content_layout.addWidget(continue_button, self.main_content_layout.rowCount() + 1, 1, 1, 1, Qt.AlignLeft | Qt.AlignBottom)
        self.main_content_layout.setAlignment(continue_button, Qt.AlignLeft | Qt.AlignBottom)

        # Add spacers to create space between button and bottom/left edges
        self.main_content_layout.addItem(QSpacerItem(125, 0, QSizePolicy.Fixed, QSizePolicy.Minimum), self.main_content_layout.rowCount(), 0)
        self.main_content_layout.addItem(QSpacerItem(0, 145, QSizePolicy.Minimum, QSizePolicy.Fixed), self.main_content_layout.rowCount() + 1, 0)

        central_widget = QWidget()
        central_widget.setObjectName("central_widget")
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def load_stylesheet(self):
        stylesheet = QFile("Styles/style.qss")
        if stylesheet.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(stylesheet)
            self.setStyleSheet(stream.readAll())

    def show_colorize_page(self):
        self.main_content.set_background_image("assets/component_bg/colorize_page_bg.png")
        self.clear_main_layout()

        v_layout = QVBoxLayout()

        title_label = QLabel("<H2>Image colorization  using GAN</H2>")
        title_label.setAlignment(Qt.AlignTop)
        title_label.setStyleSheet("font-size: 24px; color: #ffffff; margin-bottom: 20px;")
        v_layout.addWidget(title_label)

        model_path_label = QLabel("<h5>      Model Path: app/model/model.h5</h5>")
        model_path_label.setStyleSheet("font-size: 16px; color: #c6c6c6; margin-bottom: 20px;")
        model_path_label.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(model_path_label)

        gpu_info_label = QLabel(
            "<b><ul><li>Device: GPU:0 with 1654 MB memory</li><li>NVIDIA GeForce RTX 3050 Laptop GPU</li><li>Compute capability: 8.6</li><li>Loaded cuDNN version 8302</li></ul></b>")
        gpu_info_label.setStyleSheet("font-size: 13px; color: #ffa6fa;")
        gpu_info_label.setAlignment(Qt.AlignCenter)
        v_layout.addWidget(gpu_info_label)

        h_layout_for_image_labels = QHBoxLayout()

        gl_label = QLabel("Select Grey scale Image:")
        gl_label.setAlignment(Qt.AlignCenter)
        gl_label.setStyleSheet("font-size: 16px; color: #c6c6c6; margin-bottom: 10px; font-weight: bold;")
        h_layout_for_image_labels.addWidget(gl_label)

        color_label = QLabel("Color Image")
        color_label.setAlignment(Qt.AlignCenter)
        color_label.setStyleSheet("font-size: 16px; color: #6ce87d; margin-bottom: 10px; font-weight: bold;")
        h_layout_for_image_labels.addWidget(color_label)

        h_layout_for_image_labels_widget = QWidget()
        h_layout_for_image_labels_widget.setLayout(h_layout_for_image_labels)
        v_layout.addWidget(h_layout_for_image_labels_widget)

        h_layout_for_images = QHBoxLayout()

        # image display
        gl_image = QLabel()
        gl_image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("assets/image_dummies/grey_dummy.png")
        gl_image.setPixmap(pixmap.scaled(256, 256, Qt.KeepAspectRatio))
        h_layout_for_images.addWidget(gl_image)

        color_image = QLabel()
        color_image.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("assets/image_dummies/color_dummy.png")
        color_image.setPixmap(pixmap.scaled(256, 256, Qt.KeepAspectRatio))
        h_layout_for_images.addWidget(color_image)

        h_layout_for_images_widget = QWidget()
        h_layout_for_images_widget.setLayout(h_layout_for_images)
        v_layout.addWidget(h_layout_for_images_widget)

        button_layout = QHBoxLayout()
        button_font = QFont("Railway", 8, QFont.Bold)

        clear_button = QPushButton("CLEAR")
        clear_button.clicked.connect(lambda: self.show_colorize_page())
        clear_button.setObjectName("buttons")
        clear_button.setFont(button_font)
        button_layout.addWidget(clear_button)

        browse_button = QPushButton("BROWSE")
        browse_button.setObjectName("buttons")
        browse_button.setFont(button_font)
        browse_button.clicked.connect(lambda: self.browse_gl_image())
        button_layout.addWidget(browse_button)

        colorize_button = QPushButton("COLORIZE")
        colorize_button.setObjectName("buttons")
        colorize_button.setFont(button_font)
        colorize_button.clicked.connect(lambda: self.browse_gl_image())
        button_layout.addWidget(colorize_button)

        download_button = QPushButton("DOWNLOAD")
        download_button.setObjectName("download_button")
        download_button.setFont(button_font)
        #download_button.setEnabled(False)
        download_button.clicked.connect(lambda: self.browse_gl_image())
        button_layout.addWidget(download_button)

        button_layout_widget = QWidget()
        button_layout_widget.setLayout(button_layout)
        v_layout.addWidget(button_layout_widget)

        main_widget = QWidget()
        main_widget.setLayout(v_layout)
        self.main_content_layout.addWidget(main_widget)

    def clear_main_layout(self):
        while self.main_content_layout.count():
            child = self.main_content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def browse_gl_image(self):
        pass


try:
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    window = MainAppWindow()
    window.load_stylesheet()
    window.show()
    sys.exit(app.exec_())
except Exception as e:
    print(e)
