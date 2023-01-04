from unicodedata import name
from suministro import Suministro
from parametros import (
    AFINIDAD_HIT,
    AFINIDAD_INICIAL,
    AFINIDAD_PUBLICO_POP,
    AFINIDAD_STAFF_POP,
    AFINIDAD_PUBLICO_ROCK,
    AFINIDAD_STAFF_ROCK,
    AFINIDAD_PUBLICO_TRAP_CHILENO,
    AFINIDAD_STAFF_TRAP_CHILENO,
    AFINIDAD_PUBLICO_REG,
    AFINIDAD_STAFF_REG,
    AFINIDAD_ACCION_POP,
    AFINIDAD_ACCION_ROCK,
    AFINIDAD_ACCION_TRAP_CHILENO,
    AFINIDAD_ACCION_REG,
    AFINIDAD_MIN,
    AFINIDAD_MAX,
)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion, hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        if self._afinidad_con_publico < AFINIDAD_MIN:
            self._afinidad_con_publico = 0
        elif self._afinidad_con_publico > AFINIDAD_MAX:
            self._afinidad_con_publico = 100
        return self._afinidad_con_publico

    @property
    def afinidad_con_staff(self):
        if self.afinidad_con_staff < AFINIDAD_MIN:
            self.afinidad_con_staff = 0
        elif self.afinidad_con_staff > AFINIDAD_MAX:
            self.afinidad_con_staff = 100
        return self._afinidad_con_staff

    @property
    def animo(self):
        animo = (self._afinidad_con_publico * 0.5) + int(
            self._afinidad_con_staff * 0.5
        )
        

    def recibir_suministros(self, suministro):
        suministro_staf = self._afinidad_con_staff + suministro.valor_de_satisfaccion
        self._afinidad_con_staff = suministro_staf
        if suministro_staf < self._afinidad_con_staff:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones")
        else:
            print(f"{self.nombre} recibió {suministro.nombre} a tiempo")

    def cantar_hit(self):
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")

    def __str__(self):
        return f"Artista {str(self.nombre)}, su genero es {self.genero} y sus animos son {self.animo}"


class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP
        self.accion = "Cambio de vestuario"

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}!")
        self._afinidad_con_publico += AFINIDAD_ACCION_POP

    def animo(self, nuevo_valor):
        valor = super().animo
        if valor < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {valor}")
        return valor


class ArtistaRock(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Solo de guitarra"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}!")
        self._afinidad_con_publico += AFINIDAD_ACCION_ROCK

    def animo(self, nuevo_valor):
        valor = super().animo
        if valor < 20:
            print(f"ArtistaRock peligrando en el concierto. Animo: {valor}")
        return valor


class ArtistaTrapChileno(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Malianteo"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_TRAP_CHILENO
        self._afinidad_con_staff = AFINIDAD_STAFF_TRAP_CHILENO

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}!")
        self._afinidad_con_publico += AFINIDAD_ACCION_TRAP_CHILENO

    def animo(self):
        valor_animo = int(self.animo)
        if self.animo < 20:
            print(f"ArtistaTrapChileno peligrando en el concierto. Animo: {valor_animo}")
        self.animo = valor_animo
        return self.animo

class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.accion = "Perrear"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self._afinidad_con_staff = AFINIDAD_STAFF_REG

    def accion_especial(self):
        print(f"{self.nombre} hará un {self.accion}!")
        self._afinidad_con_publico += AFINIDAD_ACCION_REG

    def animo(self):
        valor_animo = int(self.animo)
        if self.animo < 2:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {valor_animo}")
        self.animo = valor_animo
        return self.animo
