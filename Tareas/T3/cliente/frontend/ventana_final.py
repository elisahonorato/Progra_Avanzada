"""
Instanciamos la ventana principal de PYQT
"""
import sys
from PyQt5 import uic, QtCore
from PyQt5.QtCore import pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from os.path import join
from utils import data_json
from PyQt5.QtMultimedia import QSound
from time import sleep

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_PANTALLA_FINAL")))


class VentanaFinal(window_name, base_class):
    
    senal_volver = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_gui()
        self.carta = None

    def init_gui(self):
        self.widget = QWidget()
        self.vbox = QVBoxLayout()    
        self.boton_volver.clicked.connect(self.volver)    

    def mostrar(self, resultado):
        if resultado == "ganador": 
            self.label_texto.setText("Has Ganado")
        elif resultado == "perdedor":
            self.label_texto.setText("Has Perdido")
        self.show()

    def volver(self):
        self.close()
        self.senal_volver.emit()

    def ocultar(self):
        self.hide()

    def salir(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaFinal()
    ventana.mostrar()
    sys.exit(app.exec_())