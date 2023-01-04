from parametros import VIDA_PEKKA, RECUPERACION_VIDA_PEKKA, ORO_INICIAL, \
    PONDERADOR_BARBAROS
from threading import Lock


class CentroUrbano:
    lock_oro = Lock()
    lock_chozas = Lock()
    def __init__(self) -> None:
        with self.lock_oro:
            self.oro = ORO_INICIAL
        with self.lock_chozas:
            self.chozas = 0
       

    @property
    def barbaros(self) -> int:
        return int(self.chozas * PONDERADOR_BARBAROS)
