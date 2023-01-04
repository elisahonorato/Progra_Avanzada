from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QKeyEvent
import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_PRINCIPAL)

class VentanaPrincipal(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_enviar_escena = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setupUi(self)
        self.init_gui()
        
    def init_gui(self):
        self.setStyleSheet(f"background-image: url({p.RUTA_FONDO});")
        self.setGeometry(600, 200, p.INTERFAZ_ANCHO + 500, p.INTERFAZ_ALTO)
        self.setWindowTitle('Ventana de Principal')
        
        # Escenas
        self.label_abuela.setStyleSheet(f"background-image: url({p.RUTA_FONDO_ABUELA});")
        self.label_nocturno.setStyleSheet(f"background-image: url({p.RUTA_FONDO_NOCTURNO});")
      
        # Botones
        self.boton_abuela.setStyleSheet('selection-background-color: aqua;')
        self.boton_nocturno.setStyleSheet('selection-background-color: aqua;')
 
        self.boton_plantar.clicked.connect(self.enviar_escena)
        
    def mostrar_ventana(self):
        self.show()
        
    def enviar_escena(self):
        self.senal_enviar_escena.emit({"boton_abuela":self.boton_abuela.isChecked(),"boton_nocturno": self.boton_nocturno.isChecked()})

    def recibir_validacion(self, valid: bool):
        if valid:
            self.hide()
            self.label_error.setText("")
        elif not valid:
            self.label_error.setText(f"Selecciona sólo una escena")
        self.boton_abuela.setChecked(False)
        self.boton_nocturno.setChecked(False)
        
    def iniciar_juego(self):
        self.senal_iniciar_juego.emit()
        self.hide()
        

        