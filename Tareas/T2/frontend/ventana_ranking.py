from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKING)


class VentanaRanking(window_name, base_class):

    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.puntaje = 0
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        self.setStyleSheet(f"background-image: url({p.RUTA_FONDO});")
        self.setGeometry(600, 200, p.INTERFAZ_ANCHO, p.INTERFAZ_ALTO)
        self.setWindowTitle("Ventana Ranking")
        
        # Botones
        self.boton_volver.clicked.connect(self.volver_inicio)
        self.icono_sol.setStyleSheet(f"background-image: url({p.RUTA_ICONO_SOL}); background-repeat: no-repeat; background-position: center;")
        self.icono_sol.resize(20,20)
        

    def volver_inicio(self):
        self.senal_volver_inicio.emit()
        self.hide()

    def abrir(self, datos: dict):
        self.show()
        self.puntaje = datos['Puntaje']
        self.label_puntaje.setText(datos['Puntaje'])
        self.label_puntaje.repaint()

