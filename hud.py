import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QGuiApplication


class Text_epta(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)


        self.subtitle_label = QLabel("Ну что, наигрался уже?\
                                     Может пора начать учиться")
        self.subtitle_label.setWordWrap(True)
        self.subtitle_label.setFixedWidth(260)
        self.subtitle_label.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 100);
                color: #000000;
                border: 1px solid #000012;
                border-radius: 12px;
                padding: 12px;
                font-family: 'Segoe UI', Arial;
                font-size: 13px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.subtitle_label)


class Makise_img(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        

        self.image_label = QLabel(self)
        pixmap = QPixmap("assets/m-removebg-preview.png")
        pixmap = pixmap.scaledToHeight(350, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.image_label)

        self.bubble = Text_epta()
        self.bubble.show()
        self.okoshki()

    def okoshki(self):
        self.adjustSize()
        screen = QGuiApplication.primaryScreen().availableGeometry()
        kurisu_x = screen.width() - self.width()
        kurisu_y = screen.height() - self.height()
        self.move(kurisu_x, kurisu_y)

        self.bubble.adjustSize()
        self.bubble.move(1470, 670)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F1:
            self.image_label.close()
            self.bubble.close()
            
        
