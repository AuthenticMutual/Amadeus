import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QGuiApplication, QMovie
from voice_recognition import VoiceInput


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
        self.pixmap = QPixmap("assets/m-removebg-preview.png")
        self.pixmap = self.pixmap.scaledToHeight(350, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(self.pixmap)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.image_label)

        self.bubble = Text_epta()
        self.bubble.show()
        self.okoshki()

        self.voice = VoiceInput()
        self.voice.finished_text.connect(self.on_voice_ready)


    def on_voice_ready(self, text):
        self.bubble.subtitle_label.setText(f"Ты сказал: «{text}»")
        self.okoshki()

    def okoshki(self):
        self.adjustSize()
        screen = QGuiApplication.primaryScreen().availableGeometry()
        kurisu_x = screen.width() - self.width()
        kurisu_y = screen.height() - self.height()
        self.move(kurisu_x, kurisu_y)

        self.bubble.adjustSize()
        bubble_x = kurisu_x - self.bubble.width() + 50
        bubble_y = kurisu_y +60
        self.bubble.move(bubble_x, bubble_y)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F1:
            QApplication.quit()
        elif event.key() == Qt.Key.Key_F2:
            if not self.voice.isRunning():
                self.bubble.subtitle_label.setText("Слушаю... Говори.")
                self.okoshki()
                self.voice.start()