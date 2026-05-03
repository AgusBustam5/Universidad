import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QKeyEvent

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.crear_gui()

    def crear_gui(self):
        self.teclas_presionadas = set()
        self.estado = QLabel("Actualmente no se presiona ninguna tecla", self)
        self.estado.move(20,10)
        self.resize(self.estado.sizeHint())

        self.setGeometry(300, 300, 600, 150)
        self.setWindowTitle("Teclado ?")
        self.show()

    def keyPressEvent(self, event: QKeyEvent):

            nuevo_texto = event.text()
            nuevo_codigo = event.key()
            self.teclas_presionadas.add((nuevo_texto, nuevo_codigo))

            self.estado.setText(f"Presionaron las teclas: {list(self.teclas_presionadas)}")
            self.estado.resize(self.estado.sizeHint())

    def keyReleaseEvent(self, event: QKeyEvent):

            texto_eliminado = event.text()
            codigo_eliminado = event.key()
            self.teclas_presionadas.remove((texto_eliminado, codigo_eliminado))
            if len(self.teclas_presionadas) == 0:
                self.estado.setText("No se esta presionando ninguna tecla actualmente")
            else:
                self.estado.setText(f"Presionaron las teclas: {list(self.teclas_presionadas)}")
            self.estado.resize(self.estado.sizeHint())
    

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())