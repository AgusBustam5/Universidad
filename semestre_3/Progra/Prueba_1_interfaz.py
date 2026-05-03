import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        #Definir geometria ventana
        #Parametros: (x_sup_izq, y_sup_izq, ancho, alto)

        self.init_gui()

    def init_gui(self):
        #Forma
        self.setGeometry(200, 100, 200, 300)
        #Titulo
        self.setWindowTitle("Papelucho Mi Primera Ventana")

        self.label1 = QLabel("Texto", self)
        self.label1.move(10,15)

        self.label2 = QLabel("Etiqueta  Variable", self)
        self.label2.move(10, 50)

        self.edit = QLineEdit("prueba de textito", self)
        self.edit.setGeometry(50, 15, 100, 20)
        self.show



if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook_ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    print(ventana.pos())
    codigo = app.exec()


    print(f"Exit code: {codigo}")
    sys.exit(codigo)