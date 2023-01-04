"""
Instanciamos la ventana login de PYQT
"""
import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from os.path import join
from utils import data_json


window_name, base_class = uic.loadUiType(join(*data_json(
                                                        "RUTA_PANTALLA_LOGIN")))


class VentanaLogin(window_name, base_class):

    senal_enviar_login = pyqtSignal(dict)
    senal_mostrar_ventana_principal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.estado = False
        self.init_gui()

    def init_gui(self):
        # CONECCIONES
        self.boton.clicked.connect(self.enviar_login)
        self.mostrar()

    def keyPressEvent(self, event):
        """Si apreta Enter se envia al servidor"""
        if event.key() == Qt.Key_Return:
            self.enviar_login()

    def enviar_login(self):
        """Cuando se apreta el botón de enviar o se apreta enter"""
        nombre_usuario = self.usuario.text()
        diccionario = {
            "comando": "validar_login",
            "nombre_usuario": nombre_usuario,
        }
        self.senal_enviar_login.emit(diccionario)
        nombre_usuario = self.usuario.text().replace(" ", "")
    
    def mostrar_espera(self, str):
        self.fondo_img.setPixmap(QPixmap("sprites/background/door_pressed.png"))
        self.show()

    def mostrar_error(self):
        self.error.setText("Datos inválidos")
        self.mostrar()
        
    def mostrar(self):
        self.estado = True
        self.show()

    def ocultar(self):
        self.hide()

    def salir(self):
        self.estado = False
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaLogin()
    sys.exit(app.exec_())
