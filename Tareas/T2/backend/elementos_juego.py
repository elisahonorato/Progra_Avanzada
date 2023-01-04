from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QEventLoop, QRect
from PyQt5.QtGui import QKeyEvent, QPixmap
from PyQt5.QtWidgets import QLabel
from random import randint
import parametros as p

class Guisante(QObject):
    
    def __init__(self, tuple):
        super().__init__()
        self.frame = QLabel("")
        self.pos = QRect(tuple[0], tuple[1], 20, 20)
        self.tipo = None
        self.visible = True
        self.timer_avanzar = QTimer()
        self.timer_avanzar.setInterval(20)
        self.timer_avanzar.timeout.connect(self.animacion)
        self.sprite = ''

    def animacion(self):
        self.pos.moveTo(int(self.pos.x() + 2), int(self.pos.y()))

    def start_timer(self):
        self.timer_avanzar.start()

    def check_hit(self):
        self.toggle_hide()

    def toggle_hide(self):
        self.visible = False
class Sol(QObject):
    
    def __init__(self, pos):
        super().__init__()
        self.frame = QLabel("")
        self.pos = pos
        self.tipo = None
        self.visible = True
        self.timer_avanzar = QTimer()
        self.timer_avanzar.setInterval(200)
        self.timer_avanzar.timeout.connect(self.animacion)
        self.timer_avanzar.start()
        

    def animacion(self):
        self.pos.moveTo(self.pos.x(), int(self.pos.y() + 1))
        if self.pos.y() == 300:
            self.toggle_hide()

    def start_timer(self):
        self.timer_avanzar.start()

    def check_hit(self):
        self.toggle_hide()

    def toggle_hide(self):
        self.visible = False


class Planta(QObject):
    ruta_imagen = None

    def __init__(self):
        super().__init__()
        self.frame = QLabel("")
        self.pos = QRect(150, 200, 30, 30)
        self.visible = True
        self.ataque = False
        self.disparo = 0
        self.vida = p.VIDA_PLANTA
        self.__vida = self.vida
        self.guisante = Guisante
        self.sprite = ''
        self.instanciar_timer()

    def instanciar_timer(self):
        pass
    
    def start_timer(self):
        pass

    def animacion(self):
        pass
    

    def disparar(self, Zombie):
        self.ataque = True
        Zombie.vida -=  self.disparo
    
    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor < 0:
            self.__vida = 0
            self.visible = False
        else:
            self.__vida = nuevo_valor

class PlantaGirasol(Planta):
    tipo = "girasol"
    costo = 50
    ruta_imagen = p.RUTA_PLANTA_GIRASOL

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disparo = p.DANO_PROYECTIL
        self.vida = p.VIDA_PLANTA
        self.soles = []
        self.ruta_imagen = p.RUTA_PLANTA_GIRASOL
        self.ataque = False
        self.instanciar_timer()

    def mover(self, tuple):
        self.timer_soles_girasol.start()
        self.pos.moveTo(tuple[0], tuple[1])

    def instanciar_timer(self):
        self.timer_soles_girasol = QTimer()
        self.timer_soles_girasol.setInterval(p.INTERVALO_SOLES_GIRASOL)
        self.timer_soles_girasol.timeout.connect(self.generar_soles)

    def generar_soles(self):
        pos = (self.pos.x() + randint(-5, 5),
                   self.pos.y() - 12, 30, 30)
        sol = Sol(pos)
        self.soles.append(sol)


class PlantaClasica(Planta):
    tipo = "clasica"
    costo = 100
    ruta_imagen = p.RUTA_PLANTA_CLASICA

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disparo = p.DANO_PROYECTIL
        self.vida = p.VIDA_PLANTA
        self.instanciar_timer()

    def instanciar_timer(self):
        self.timer_disparo = QTimer()
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
        self.timer_disparo.timeout.connect(self.animacion)
    
    def start_timer(self):
        self.ataque = False
        self.timer_disparo.start()

    def animacion(self):
        self.ataque = True

    def mover(self, tuple):
        self.pos.moveTo(tuple[0], tuple[1])
        self.guisante = Guisante(tuple)


class PlantaAzul(Planta):
    tipo = "azul"
    costo = 150

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disparo = p.DANO_PROYECTIL
        self.vida = p.VIDA_PLANTA
        self.instanciar_timer()

    def instanciar_timer(self):
        self.timer_disparo = QTimer()
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
        self.timer_disparo.timeout.connect(self.animacion)
    
    def start_timer(self):
        self.ataque = False
        self.timer_disparo.start()


    def animacion(self):
        self.ataque = True


    def mover(self, tuple):
        self.pos.moveTo(tuple[0], tuple[1])
        self.guisante = Guisante(tuple)


class PlantaPapa(Planta):
    tipo = "papa"
    costo = 75

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disparo = p.DANO_PROYECTIL
        self.vida = int(p.VIDA_PLANTA * 2)
        self.ataque = False
        self.instanciar_timer()

    def instanciar_timer(self):
        self.timer_disparo = QTimer()
        self.timer_disparo.setInterval(p.INTERVALO_DISPARO)
        self.timer_disparo.timeout.connect(self.animacion)
    
    def start_timer(self):
        self.timer_disparo.start()


    def animacion(self):
        self.ataque = True


    def mover(self, tuple):
        self.pos.moveTo(tuple[0], tuple[1])
        self.guisante = Guisante(tuple)

class Zombie(QObject):

    def __init__(self, pos):
        super().__init__()
        self.frame = QLabel("")
        self.pos = QRect(*pos)
        self.vida = p.VIDA_ZOMBIE
        self.dano = p.DANO_MORDIDA
        self.visible = True
        self.vivo = True
        self.adentro = False
        self.sprite = ''
        self.ralentizado = False
        self.instanciar_timer()

    def instanciar_timer(self):
        self.timer_avanzar = QTimer()
        self.timer_avanzar.timeout.connect(self.animacion)
        self.timer_morder = QTimer()
        self.timer_morder.setInterval(p.INTERVALO_TIEMPO_MORDIDA)

    def start_timer(self):
        self.timer_avanzar.start()
    
    def start_mordida(self):
        self.timer_morder.start()

    def animacion(self):
        self.pos.moveTo(
            int(self.pos.x() - 20), self.pos.y())
        if self.pos.x() < 779:
            self.adentro = True

    def morder(self, planta):
        self.timer_avanzar.stop()
        planta.vida -= self.dano
        if planta.vida == 0:
            self.timer_avanzar.start()
        

    def mover(self, tuple):
        self.pos.moveTo(tuple[0], tuple[1])


class ZombieClasico(Zombie):
    tipo = "clasico"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocidad = p.VELOCIDAD_ZOMBIE
        self.timer_avanzar.setInterval(self.velocidad)
        self.timer_avanzar.start()
        self.vida = p.VIDA_ZOMBIE
        self.__vida = self.vida

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor < 0:
            self.visible = False
            self.vivo = False
            self.__vida = 0
        else:
            self.__vida = nuevo_valor


class ZombieRapido(Zombie):
    tipo = "rapido"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocidad = int(p.VELOCIDAD_ZOMBIE*1.5)
        self.timer_avanzar.setInterval(self.velocidad)
        self.timer_avanzar.start()
        self.vida = p.VIDA_ZOMBIE
        self.__vida = self.vida

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nuevo_valor):
        if nuevo_valor < 0:
            self.visible = False
            self.vivo = False
            self.__vida = 0
        else:
            self.__vida = nuevo_valor
