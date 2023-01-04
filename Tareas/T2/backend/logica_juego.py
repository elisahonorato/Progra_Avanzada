from collections import deque
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QEventLoop, QRect
from backend.elementos_juego import Planta, PlantaGirasol, PlantaClasica, PlantaAzul, PlantaPapa, Sol, Zombie, ZombieClasico, ZombieRapido
from aparicion_zombies import intervalo_aparicion
from random import randint, choice
import parametros as p
import time
from PyQt5.QtWidgets import QLabel


class LogicaJuego(QObject):

    # Señal para abrir ventana puntaje
    senal_termino_juego = pyqtSignal(str, str, str, str, str, bool, list)
    senal_actualizar = pyqtSignal(str, str, str)
    senal_update_position = pyqtSignal(dict)
    senal_tiempo = pyqtSignal(str)
    senal_soles = pyqtSignal(list)
    senal_cerrar_ventana_juego = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.teclas = deque()
        self.usuario = Usuario()
        self.puntaje = 0
        self.soles = []
        self.timers = []
        self.planta = deque()
        self.zombies_carril_1 = []
        self.zombies_carril_2 = []

        self.plantas_carril_1 = []
        self.plantas_carril_2 = []
        self.plantas = []

        self.zombies = []
        self.escena = Escena()

    @property
    def puntaje(self):
        return self._puntaje

    @puntaje.setter
    def puntaje(self, valor):
        if valor <= 0:
            self._puntaje = 0
        else:
            self._puntaje = valor

    def instanciar_timer(self):
        self.timer_ronda = QTimer()
        self.timer_ronda.timeout.connect(self.terminar_juego)
        self.timer_ronda.setSingleShot(True)
        
        self.timer_actualizar_juego = QTimer()
        self.timer_actualizar_juego.setInterval(200)
        self.timer_actualizar_juego.timeout.connect(self.actualizar_juego)

        self.timer_ataque = QTimer()
        self.timer_ataque.setInterval(2000)
        self.timer_ataque.timeout.connect(self.ataque)

        self.timer_soles = QTimer()
        self.timer_soles.setInterval(p.INTERVALO_APARICION_SOLES)
        self.timer_soles.timeout.connect(self.generar_soles)

        self.timer_zombies = QTimer()
        intervalo = int(intervalo_aparicion(
            self.usuario.ronda_actual, self.escena.ponderador)*1000)
        self.timer_zombies.setInterval(intervalo)
        self.timer_zombies.timeout.connect(self.generar_zombies)

        self.timers.append(self.timer_actualizar_juego)
        self.timers.append(self.timer_ataque)
        self.timers.append(self.timer_soles)
        self.timers.append(self.timer_zombies)

    def iniciar_juego(self, usuario, escena):
        if escena == "boton_nocturno":
            self.escena = SalidaNocturna()
        elif escena == "boton_abuela":
            self.escena = JardinAbuela()
        self.usuario.nombre = usuario
        self.actualizar_juego()

    def iniciar_ronda(self):
        self.usuario.ronda_actual += 1
        self.instanciar_timer()

        for timer in self.timers:
            timer.start()

        for zombie in self.zombies:
            zombie.start_timer()

    def terminar_juego(self):
        if self.usuario.zombies_destruidos == (p.N_ZOMBIES * 2):
            gano = True
        else:
            gano = False
        self.usuario.puntaje_acumulado += self.puntaje
        self.senal_termino_juego.emit(str(self.usuario.ronda_actual), str(self.usuario.cantidad_soles), str(self.usuario.zombies_destruidos), str(self.puntaje), str(self.usuario.puntaje_acumulado), gano, [self.usuario, self.escena])

    def generar_soles(self):
        if str(self.escena.__class__.__name__) != "SalidaNocturna":
            pos = (randint(150, 900), 0, 30, 30)
            sol = Sol(pos)
            self.senal_update_position.emit(self.generar_dict(sol))
            self.soles.append(sol)

    def generar_zombies(self):
        zombie = ''
        pos_carril = choice(((789 + randint(10, 60), 120 + randint(0, 20), 40, 30), (789 + randint(10, 60), 171 + randint(0, 20), 40, 30)))
        tipo_zombie = choice((ZombieClasico, ZombieRapido))
        zombie = tipo_zombie(pos_carril)
        if zombie.pos.y() > 170 and len(self.zombies_carril_1) < p.N_ZOMBIES:
            self.zombies_carril_2.append(zombie)
        
        elif zombie.pos.y() <= 170 and len(self.zombies_carril_2) < p.N_ZOMBIES:
            self.zombies_carril_1.append(zombie)
        if zombie!= '':
            self.zombies.append(zombie)

        elif pos_carril == 2:
            pos = (789 + randint(10, 60), 171 + randint(0, 20), 40, 30)
            zombie = tipo_zombie(pos)
            if len(self.zombies_carril_2) < p.N_ZOMBIES:
                self.zombies_carril_2.append(zombie)
                self.usuario.zombies_totales +=1
                self.zombies.append(zombie)

    def ataque(self):
        for planta in (self.plantas):
            for zombie in self.zombies:
                if planta.tipo!= "girasol":
                    planta.disparar(zombie)
                    planta.guisante.start_timer()
                    self.senal_update_position.emit(self.generar_dict(planta.guisante))
                    if planta.guisante.pos.x() >= zombie.pos.x():
                        planta.guisante.sprite = "Bang"
                        self.senal_update_position.emit(self.generar_dict(planta.guisante))
                        planta.guisante.check_hit()
                        zombie.vida -= planta.disparo
                        self.actualizar_juego()
                        self.senal_update_position.emit(self.generar_dict(planta.guisante))
                        
                    if planta.ataque and planta.tipo == "azul" and not zombie.ralentizado:
                        zombie.ralentizado = True
                        zombie.velocidad*= p.RALENTIZAR_ZOMBIE

                if zombie.pos.intersects(planta.pos):
                    zombie.morder(planta)
            self.senal_update_position.emit(self.generar_dict(zombie))
            self.senal_update_position.emit(self.generar_dict(planta))
            
                       
    def actualizar_juego(self):
        for zombie in self.zombies:
            if not zombie.visible:
                self.usuario.zombies_destruidos +=1
            self.senal_update_position.emit(self.generar_dict(zombie))
        if self.usuario.zombies_destruidos == 14:
            self.terminar_juego()
        if len(self.zombies) >= 14:
            self.timer_zombies.stop()
        self.senal_actualizar.emit(str(self.usuario.cantidad_soles), str(self.usuario.zombies_destruidos), str(
            (p.N_ZOMBIES*2) - self.usuario.zombies_destruidos))

        for planta in self.plantas:
            if planta.tipo == "girasol":
                for sol in planta.soles:
                    if sol.visible == True:
                        self.soles.append(sol)
                    if sol.visible == False:
                        planta.soles.remove(sol)
                    self.senal_update_position.emit(self.generar_dict(sol))
        for sol in self.soles:
            self.senal_update_position.emit(self.generar_dict(sol))
            
    def recolectar_soles(self, posicion):
        for sol in self.soles:
            click = QRect(posicion[0], posicion[1],
                          sol.pos.width(), sol.pos.height())
            if click.intersects(QRect(sol.pos.x(), sol.pos.y(), sol.pos.width(), sol.pos.height())) and sol.visible:
                self.usuario.cantidad_soles += p.SOLES_POR_RECOLECCION
                sol.check_hit()
                self.senal_update_position.emit(self.generar_dict(sol))
                break
    

    def recibir_teclas(self, str):
        if len(self.teclas) < 4:
            if len(self.teclas) < 3:
                self.teclas.append(str)
            if len(self.teclas) == 3:
                if self.teclas == deque(["s", "u", "n"]):
                    self.usuario.cantidad_soles += p.SOLES_EXTRA
                    self.actualizar_juego()
                elif self.teclas == deque(["k", "i", "l"]):
                    for zombie in self.zombies:
                        if zombie.visible and zombie.adentro:
                            zombie.vida = 0
                        
                    self.actualizar_juego()
                self.teclas.popleft()


    def tienda_plantas(self, accion, tipo):
        if accion == "comprar":
            tipo = tipo[0]
            if tipo == "clasica":
                planta = PlantaClasica()
            elif tipo == "girasol":
                planta = PlantaGirasol()
            elif tipo == "azul":
                planta = PlantaAzul()
            elif tipo == "papa":
                planta = PlantaPapa()
            if self.usuario.adquirir_planta(planta):
                self.usuario.cantidad_soles -= planta.costo
                self.planta.append(planta)
                

        if accion == "plantar" and len(self.planta) > 0:
            evento = tipo[0]
            posicion_y = evento[1]
            posicion_inicial = 310
            ancho_label = 47
            planta = ''
            for i in range(10):
                if evento[0] < (posicion_inicial) + ancho_label:
                    posicion_x = posicion_inicial + 10
                    break
                else:
                    posicion_inicial += ancho_label
            if len(self.planta) >= 1:
                if len(self.plantas) <= 20:
                    if posicion_y < 170:
                        posicion_y = 120
                        if posicion_x not in ((planta.pos.x()) for planta in self.plantas_carril_1):
                            planta = self.planta[0]
                            self.plantas_carril_1.append(self.planta[0])
                    elif posicion_y > 170:
                        posicion_y = 180
                        if posicion_x not in ((planta.pos.x()) for planta in self.plantas_carril_2):
                            planta = self.planta[0]
                            self.plantas_carril_2.append(self.planta[0])
                    if planta != "":
                        planta = self.planta[0]
                        planta.mover((posicion_x, posicion_y))
                        self.plantas.append(planta)
                        self.senal_update_position.emit(self.generar_dict(planta))
                        self.planta.popleft()
            self.actualizar_juego()

    def generar_dict(self, QObject) -> dict:
        nombre_clase = str(QObject.__class__.__name__)
        char = None
        sprite = None
        if "Planta" in nombre_clase:
                char = "planta"
        elif "Zombie" in nombre_clase:
            char = "zombie"
        elif "Sol" in nombre_clase:
            char = "sol"
        elif "Guisante" in nombre_clase:
            char = "guisante"

        return {
            "char": char,
            "x": QObject.pos.x(),
            "y": QObject.pos.y(),
            "tamano": (QObject.pos.width(), QObject.pos.height()),
            "frame": QObject.frame,
            "sprite": QObject.sprite,
            "tipo": QObject.tipo,
            "visible": QObject.visible,
            }
    def calcular_puntaje(self):
        self.puntaje = 2


class Usuario(QObject):
    def __init__(self):
        super().__init__()
        self.nombre = str
        self.cantidad_soles = p.SOLES_INICIALES
        self.zombies_totales = 0
        self.zombies_destruidos = 0
        self.puntaje_acumulado = 0
        self.ronda_actual = 0
    
    def adquirir_planta(self, planta):
        if self.cantidad_soles >= planta.costo:
            return True
        return False
class Escena(QObject):
    ponderador = None

    def __init__(self):
        super().__init__()


class JardinAbuela(Escena):
    ponderador = p.PONDERADOR_DIURNO

    def __init__(self):
        super().__init__()


class SalidaNocturna(Escena):
    ponderador = p.PONDERADOR_NOCTURNO

    def __init__(self):
        super().__init__()