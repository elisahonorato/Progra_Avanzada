"""
Instanciamos la ventana carga de PYQT
"""
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QLabel
from os.path import join
from utils import data_json
from time import sleep

window_name, base_class = uic.loadUiType(join(*data_json(
    "RUTA_PANTALLA_CARGA")))


class VentanaCarga(window_name, base_class):

    senal_enviar_inicio = pyqtSignal(dict)
    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.contador = data_json("VELOCIDAD_CARGA")
        self.init_gui()

    def init_gui(self):
        # ELIMINAMOS LA BARRA DE TITULO
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.boton_volver.clicked.connect(self.volver)

    def actualizar_jugador(self, str):
        self.label_jugador_1.setText(str)

    def actualizar_oponente(self, str):
        self.label_jugador_2.setText(str)
        self.iniciar_juego()
        
    def progress(self):
        if self.contador <= 0:
            self.timer.stop()
            self.enviar_inicio()
        sleep(0.1)
        self.label_contador.setText(str(self.contador))
        self.contador -= 1

    def enviar_inicio(self):
        nombre_usuario = self.label_jugador_1.text()
        diccionario = {
            "comando": "enviar_inicio",
            "nombre_usuario": nombre_usuario,
        }
        self.senal_enviar_inicio.emit(diccionario)

    def mostrar(self):
        self.show()

    def iniciar_juego(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(self.contador)

    def ocultar(self):
        self.hide()

    def volver(self):
        self.close()
        self.senal_volver.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaCarga()
    sys.exit(app.exec_())
