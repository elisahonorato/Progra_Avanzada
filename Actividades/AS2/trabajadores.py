from ast import Return
from time import sleep
from threading import Thread, Lock

from centro_urbano import CentroUrbano

from parametros import ENERGIA_RECOLECTOR, ORO_RECOLECTADO, \
    TIEMPO_RECOLECCION, TIEMPO_CONSTRUCCION, ORO_CHOZA


# Completar
class Recolector(Thread):
    def __init__(self, nombre: str, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        self.energia = ENERGIA_RECOLECTOR
        self.oro = 0
        # Completar
        self.daemon = True
        
    def run(self) -> None:
        self.trabajar()
        self.ingresar_oro()
        self.dormir()

    def log(self, mensage: str) -> None:
        print(f"El recolector {self.nombre}: {mensage}")

    def trabajar(self) -> None:
        self.log("He empezado la recolección de oro")
        while self.energia:
            self.oro += ORO_RECOLECTADO
            self.log(f"Se recolectó {ORO_RECOLECTADO} monedas de oro")
            self.energia -= 1
            sleep(TIEMPO_RECOLECCION)

    def ingresar_oro(self) -> None:
        with self.centro_urbano.lock_oro:
            self.centro_urbano.oro += self.oro
        self.oro = 0
        self.log("Deposité Oro")
        self.log(f"Hay {self.centro_urbano.oro} en el Centro Urbano")
        

    def dormir(self) -> None:
        self.log("ha terminado su turno, procede a mimir")


# Completar
class Constructor(Thread):
    def __init__(self, nombre, centro_urbano: CentroUrbano) -> None:
        super().__init__()
        self.nombre = nombre
        self.centro_urbano = centro_urbano
        # Completar
        self.daemon = True

    def run(self) -> None:
        while self.retirar_oro():
            self.log("está construyendo una choza de bárbaros")
            sleep(TIEMPO_CONSTRUCCION)
            self.construir_choza()
        self.log("terminó su trabajo por el día")

    def log(self, mensage: str) -> None:
        print(f"El constructor {self.nombre}: {mensage}")

    def retirar_oro(self) -> bool:
        if self.centro_urbano.oro >= ORO_CHOZA:
            with self.centro_urbano.lock_oro:
                self.centro_urbano.oro -= ORO_CHOZA
            self.log(f"Quedan {self.centro_urbano.oro} unidades de oro en Centro Urbano")
            return True
        elif self.centro_urbano.oro < ORO_CHOZA:
            self.log ("No se pudo retirar oro")
            return False
            

    def construir_choza(self) -> None:
        with self.centro_urbano.lock_chozas:
            self.centro_urbano.chozas += 1
            print(f"Agregué una choza {self.centro_urbano.chozas}")

