from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

import parametros as p
window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_INICIO)

class VentanaInicio(window_name, base_class):

    senal_enviar_login = pyqtSignal(str)
    senal_ver_ranking = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        # Geometría
        self.setupUi(self)
        self.init_gui()
        
    def init_gui(self):
        self.setStyleSheet(f"background-image: url({p.RUTA_FONDO});")
        self.setGeometry(600, 200, p.INTERFAZ_ANCHO, p.INTERFAZ_ALTO)
        self.setWindowTitle('Ventana de Inicio')
        
        # Logo
        self.widget_logo.setStyleSheet(f"background-image: url({p.RUTA_LOGO}); background-repeat: no-repeat; background-position: center;")
    
        # Botones
        self.boton_usuario.setPlaceholderText("Ingrese Usuario:") 
        self.boton_jugar.clicked.connect(self.enviar_login)
        self.boton_ranking.clicked.connect(self.ver_ranking)
        self.boton_salir.clicked.connect(self.close)
        self.show()

    def ver_ranking(self):
        self.senal_ver_ranking.emit()
        self.hide()
        
    def enviar_login(self):
        self.senal_enviar_login.emit(self.boton_usuario.text())
        self.boton_usuario.setText("")

    def recibir_validacion(self, valid: bool, errores: list):
        if valid:
            self.hide()
            self.label_error.setText("")
        elif not valid:
            self.boton_usuario.setPlaceholderText("Usuario Inválido")
            self.label_error.setText(f"{[(error) for error in errores]}")
            self.label_error.setText("")

