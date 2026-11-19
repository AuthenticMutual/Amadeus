import sys
from PyQt6.QtWidgets import QApplication
from hud import Makise_img

if __name__ == "__main__":
    app = QApplication(sys.argv)
    def_pose = Makise_img()
    def_pose.show()
    sys.exit(app.exec())