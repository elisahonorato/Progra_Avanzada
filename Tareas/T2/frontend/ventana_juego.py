from PyQt5.QtCore import pyqtSignal
from PyQt5.QtMacExtras import *
from PyQt5 import uic, QtCore
from PyQt5.QtCore import pyqtSignal, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPixmap
from traitlets import ObjectName
from backend.elementos_juego import PlantaClasica, Zombie

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)


class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal(str, str)
    senal_volver_inicio = pyqtSignal()
    senal_iniciar_ronda = pyqtSignal()
    senal_tecla = pyqtSignal(str)
    senal_mouse_izquierdo = pyqtSignal(str, list)
    senal_mouse_derecho = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setupUi(self)
        self.init_gui()
        self.dict_plantas = {
            "planta_girasol": {"pos": (0, 99), "tipo": "girasol"},
            "planta_clasica": {"pos": (100, 199), "tipo": "clasica"},
            "planta_azul": {"pos": (200, 299), "tipo": "azul"},
            "planta_papa": {"pos": (300, 399), "tipo": "papa"}}
        self.dict_pos = {"pos_tienda": (
            0, 149), "pos_plantar": (310, 170, 800, 240), "pos_plantas": self.dict_plantas, "pos_zombies": (790, 120, 100, 240)}
        self.list_frames = []

    def init_gui(self):
        self.setGeometry(600, 200, p.INTERFAZ_ANCHO + 500, p.INTERFAZ_ALTO)

        self.setWindowTitle('Ventana de Juego')
        self.boton_iniciar.clicked.connect(self.iniciar_ronda)
        self.boton_salir.clicked.connect(self.volver_inicio)

    def mostrar_ventana(self, nombre, escena):
        # Escena
        if escena == "boton_nocturno":
            ruta_fondo = p.RUTA_FONDO_NOCTURNO
        elif escena == "boton_abuela":
            ruta_fondo = p.RUTA_FONDO_ABUELA
        pixeles = QPixmap(ruta_fondo)
        self.label_fondo_juego.setPixmap(pixeles)
        self.label_fondo_juego.setScaledContents(1)
        # Tienda

        self.show()
        self.senal_iniciar_juego.emit(nombre, escena)


    def actualizar_elementos(self, dic):
        if dic["visible"]:
            if dic["char"] == "planta":
                if dic["tipo"] == "girasol":
                    ruta = p.RUTA_PLANTA_GIRASOL
                elif dic["tipo"] == "clasica":
                    ruta = p.RUTA_PLANTA_CLASICA
                elif dic["tipo"] == "azul":
                    ruta = p.RUTA_PLANTA_AZUL
                elif dic["tipo"] == "papa":
                    ruta = p.RUTA_PLANTA_PAPA

            if dic["char"] == "zombie":
                if dic["tipo"] == "rapido":
                    ruta = p.RUTA_ZOMBIE_RAPIDO
                elif dic["tipo"] == "clasico":
                    ruta = p.RUTA_ZOMBIE_CLASICO
            if dic["char"] == "sol":
                ruta = p.RUTA_ICONO_SOL
            if dic["char"] == "guisante":
                ruta = p.RUTA_GUISANTE
            
            dic["frame"].setScaledContents(True)
            dic["frame"].setParent(self)
            dic["frame"].setPixmap(QPixmap(ruta))
            dic["frame"].resize(dic["tamano"][0], dic["tamano"][1])
      
            dic["frame"].show()
            dic["frame"].move(dic["x"], dic["y"])
            dic["frame"].show()
        self.list_frames.append(dic["frame"])

        if dic["visible"] == False:
            dic["frame"].hide()



    def actualizar_datos(self, cantidad_soles: str, zombies_destruidos: str, zombies_restantes: str):
        self.label_soles.setText(cantidad_soles)
        self.label_zombies_destruidos.setText(zombies_destruidos)
        self.label_zombies_restantes.setText(zombies_restantes)
        

    def iniciar_ronda(self):
        self.senal_iniciar_ronda.emit()

    def volver_inicio(self):
        self.senal_volver_inicio.emit()
        for frame in self.list_frames:
            frame.repaint()
            frame.hide()
            frame.close()
        self.hide()

    def keyPressEvent(self, event: QKeyEvent):
        tecla = event.text().lower()
        self.senal_tecla.emit(tecla)

    def numero_en_rango(self, valor, rango=tuple):
        if rango[0] <= valor < rango[1]:
            return True
        return False

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            accion = ""
            tipo = ""
            if self.numero_en_rango(event.x(), self.dict_pos["pos_tienda"]):
                accion = "comprar"
                if self.numero_en_rango(event.y(), self.dict_plantas["planta_girasol"]["pos"]):
                    tipo = self.dict_plantas["planta_girasol"]["tipo"]
                if self.numero_en_rango(event.y(), self.dict_plantas["planta_clasica"]["pos"]):
                    tipo = self.dict_plantas["planta_clasica"]["tipo"]
                if self.numero_en_rango(event.y(), self.dict_plantas["planta_azul"]["pos"]):
                    tipo = self.dict_plantas["planta_azul"]["tipo"]
                if self.numero_en_rango(event.y(), self.dict_plantas["planta_papa"]["pos"]):
                    tipo = self.dict_plantas["planta_papa"]["tipo"]
            if self.numero_en_rango(event.x(), (310, 789)) and self.numero_en_rango(event.y(), (120, 240)):
                tipo = (event.x(), event.y())
                accion = "plantar"

            if accion != "" and tipo != "":
                self.senal_mouse_izquierdo.emit(accion, [tipo])

        elif event.button() == QtCore.Qt.RightButton:
            self.senal_mouse_derecho.emit((event.x(), event.y()))

    def salir(self):
        self.close()

