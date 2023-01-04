from abc import ABC, abstractmethod
from random import randint
from parametros import INCREMENTO_FEROCIDAD, MAX_EX_CARNIVORO, MAX_EX_HERVIBORO, \
                        MIN_EX_CARNIVORO, MIN_EX_HERVIBORO, INCREMENTO_ADORABILIDAD, \
                        GAN_CARNIVORO, GAN_HERBIVORO



# MODIFICAR
class Animal(ABC):

    # MODIFICAR
    def __init__(self, especie: str, **kwargs):
        self.ganancia_actual = 0
        self.especie = especie

    @abstractmethod
    def alimentarse(self):
        pass

    @abstractmethod
    def exhibicion(self):
        pass

    def __str__(self):
        return f"Animal de especie {self.especie}"


# MODIFICAR
class Carnivoro(Animal):

    # MODIFICAR
    def __init__(self, especie: str, ferocidad= int, **kwargs):
        super().__init__(especie, **kwargs)
        self.ferocidad = ferocidad
        self.ganancia_actual += GAN_CARNIVORO

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.ferocidad = self.ferocidad*INCREMENTO_FEROCIDAD
        print(f"Animal {self.especie} se come un kilogramo de Carne")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        ponderador = randint(MIN_EX_CARNIVORO, MAX_EX_CARNIVORO)
        self.ganancia_actual+= self.ferocidad * ponderador


# MODIFICAR
class Herbivoro(Animal):
    
    def __init__(self, especie: str, adorabilidad = int, **kwargs):
        super().__init__(especie, **kwargs)
        self.adorabilidad = adorabilidad
        self.ganancia_actual += GAN_HERBIVORO

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        self.adorabilidad = self.adorabilidad * INCREMENTO_ADORABILIDAD
        print(f"Animal {self.especie} se come un kilogramo de vegetales")

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        ponderador = randint(MIN_EX_HERVIBORO, MAX_EX_HERVIBORO)
        self.ganancia_actual+= self.adorabilidad * ponderador

# MODIFICAR
class Omnivoro(Carnivoro, Herbivoro):

    # MODIFICAR
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ganancia_actual = 0

    # MODIFICAR
    def alimentarse(self):
        super().alimentarse()
        

    # MODIFICAR
    def exhibicion(self):
        super().exhibicion()
        

