from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtCore import QObject

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POST_RONDA)


class VentanaPostRonda(window_name, base_class):

    senal_abrir_inicio = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()
    senal_siguiente_ronda = pyqtSignal(QObject, QObject)

    def __init__(self):
        super().__init__()
        self.puntaje = 0
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("Ventana PostRonda")
        self.boton_salir.clicked.connect(self.salir)
        self.boton_siguiente_ronda.clicked.connect(self.siguiente_ronda)

    def volver_inicio(self):
        self.senal_abrir_inicio.emit()
        self.hide()

    def abrir(self, ronda, soles, zombies, puntaje_ronda, puntaje_acumulado, gano, list):
        self.label_ronda.setText(ronda)
        self.label_soles.setText(soles)
        self.label_zombies.setText(zombies)
        self.label_puntaje.setText(puntaje_ronda)
        self.label_puntaje_acumulado.setText(puntaje_acumulado)
        if gano:
            self.label_ganador.show()
            self.label_perdedor.close()
        if not gano:
            self.label_perdedor.show()
            self.label_ganador.close()
        self.list = list
        self.show()


    def siguiente_ronda(self):
        self.hide()
        self.senal_siguiente_ronda.emit(self.list[0], self.list[1])


    def salir(self):
        self.hide()
        self.senal_cerrar_juego.emit()
