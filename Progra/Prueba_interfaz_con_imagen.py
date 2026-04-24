import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

class ventana_imagen(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.init_gui()

    def init_gui(self):
        self.setGeometry(200, 100, 200, 200)
        self.setWindowTitle("Ventanuski con imagen")

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 100, 100)

        pixeles = QPixmap("/home/agusbustam/Descargas/vader.jpg")

        self.label.setPixmap(pixeles)

        self.label.setScaledContents(True)

        self.show()

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = ventana_imagen()
    sys.exit(app.exec())