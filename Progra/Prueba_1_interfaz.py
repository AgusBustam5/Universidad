import sys
from PyQt6.QtWidgets import QWidget, QApplication

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        #Definir geometria ventana
        #Parametros: (x_sup_izq, y_sup_izq, ancho, alto)
        self.setGeometry()

        self.setGeometry("Papelucho Mi Primera Ventana")

if __name__ == "main":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook_ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    codigo = app.exec()


    print(f"Exit code: {codigo}")
    sys.exit(codigo)