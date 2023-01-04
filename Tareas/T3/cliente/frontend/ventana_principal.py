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
    "RUTA_PANTALLA_PRINCIPAL")))


class VentanaPrincipal(window_name, base_class):

    senal_enviar_ronda = pyqtSignal(dict)
    senal_actualizar_usuarios = pyqtSignal(list)
    senal_iniciar_ronda = pyqtSignal()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_gui()
        self.carta = None

    def init_gui(self):
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

    def progress(self):
        if self.contador <= 0:
            self.timer_ronda.stop()
            self.enviar_ronda()
        sleep(0.3)
        self.label_contador.setText(str(self.contador))
        self.contador -= 1

    def enviar_ronda(self):
        if self.carta is None:
            self.carta = self.baraja.pop(0)
            self.label_jugador.setPixmap(QPixmap(self.carta))
        self.label_jugador.setPixmap(QPixmap(self.carta))
        sleep(0.4)
            
        diccionario = {
        "comando": "enviar_ronda",
        "carta": str(self.carta),
        "user_id": self.id,
        }
        
        self.senal_enviar_ronda.emit(diccionario)
        for boton in self.label_tabla.children():
            if boton.objectName == self.carta:
                boton.hide()
        

    def actualizar_cartas(self):
        self.label_oponente.setPixmap(QPixmap("sprites/cartas/back.png"))
        self.label_jugador.setPixmap(QPixmap("sprites/cartas/back.png"))
        self.contador = data_json("CUENTA_REGRESIVA_RONDA")
        icon_size = 60
        contador = 0
        for x in range(len(self.baraja)):
            contador += 1
            self.button = QPushButton(self.label_tabla)
            self.button.objectName = self.baraja[x]
            self.button.setGeometry(contador * 50, 340, icon_size, icon_size)
            self.button.setIcon(QIcon(self.baraja[x]))
            self.button.setIconSize(QtCore.QSize(icon_size , icon_size))
            self.button.setCheckable(True)
            self.button.clicked.connect(self.seleccionar_carta)
            self.button.show()
        self.senal_iniciar_ronda.emit()
   
        
    def seleccionar_carta(self):
        for boton in self.label_tabla.children():
            if boton.isChecked():
                boton.setCheckable(False)
                self.carta = boton.objectName
                self.label_jugador.setPixmap(QPixmap(self.carta))
            
                
    def iniciar_ronda(self, lista, id):
        self.id = id
        self.baraja = lista
        self.actualizar_cartas()
        self.timer_ronda = QTimer()
        self.timer_ronda.timeout.connect(self.progress)
        self.timer_ronda.start(self.contador)
    
    def mostrar_carta(self, carta, carta_reemplazante):
        self.label_tabla.children()[1].setIcon(QIcon(carta_reemplazante))
        self.label_oponente.setPixmap(QPixmap(carta))
        self.label_jugador.setPixmap(QPixmap(self.carta))
        self.carta = None
        sleep(0.5)
    
    def mostrar_carta_ganadora(self, cartas_ganadoras):
        icon_size = 30
        contador = 0
        for carta in cartas_ganadoras:
            contador += 1
            self.button = QPushButton(self)
            self.button.objectName = carta
            self.button.setGeometry(contador * 10, 10, icon_size, icon_size)
            self.button.setIcon(QIcon(carta))
            self.button.setIconSize(QtCore.QSize(icon_size , icon_size))
            self.button.show()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()


    def salir(self):
        self.timer_ronda.stop()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.mostrar()
    sys.exit(app.exec_())