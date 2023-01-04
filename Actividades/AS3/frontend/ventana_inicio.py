from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        margenes_logo = 200
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap(p.RUTA_LOGO))
        self.label.setGeometry(0, 0, 500, margenes_logo)
        self.label.setScaledContents(True)
        
        margenes_x = 20
        margenes_y = 20
        #Ingrese Usuario
        self.usuario_form_label = QLabel('Usuario:', self)
        self.usuario_form_label.setGeometry(margenes_x, margenes_logo + margenes_y, 200, 20)
        self.usuario_form = QLineEdit("", self)
        self.usuario_form.setGeometry(margenes_x, margenes_logo + margenes_y * 2, 200, 20)
        
        #Ingrese Clave
        self.clave_form_label = QLabel('Clave', self)
        self.clave_form_label.setGeometry(margenes_x, margenes_logo + margenes_y * 3, 200, 20)
        self.clave_form = QLineEdit("", self)
        self.clave_form.setGeometry(margenes_x, margenes_logo + margenes_y * 4, 200, 20)
        self.clave_form.setEchoMode(QLineEdit.Password)
        
        #Botón
        self.ingresar_button = QPushButton("Ingresar", self)
        self.ingresar_button.setGeometry(margenes_x, margenes_logo + margenes_y * 6, 200, 50)
        self.ingresar_button.clicked.connect(self.enviar_login)

        
        self.show()

    def enviar_login(self):
        self.senal_enviar_login.emit(self.usuario_form.text(), self.clave_form.text())
        
    def recibir_validacion(self, valid: bool, errores: set):
        if valid:
            self.hide()
        elif not valid:
            print(errores)
            if "usuario" in errores:
                self.usuario_form.setText("")
                self.usuario_form.setPlaceholderText("Usuario inválido")
            if "contraseña" in errores:
                self.clave_form.setText("")
                self.clave_form.setPlaceholderText("Contraseña inválida")