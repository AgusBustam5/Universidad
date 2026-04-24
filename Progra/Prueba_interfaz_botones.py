import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class ventana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):

        self.setGeometry(20, 10, 400, 300)
        self.setWindowTitle("Ventanuski con botones")

        self.labels = {}
        self.labels["label1"] = QLabel("Texto:", self)
        self.labels["label1"].move(10, 15)

        self.labels["label2"] = QLabel("Escbir respuesta aqui", self)
        self.labels["label2"].move(10,50)

        self.edit1 = QLineEdit("", self)
        self.edit1.setGeometry(45, 15, 100, 20)

        self.boton1 = QPushButton("&Procesar",self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(5, 70)

        self.show()

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    ventanuski = ventana()
    ventanuski.show()
    sys.exit(app.exec())