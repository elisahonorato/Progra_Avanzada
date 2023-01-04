from abc import ABC, abstractmethod
from parametros import AUMENTO_DEFENSA, ENERGIA_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA, GASTO_ENERGIA_BAYA, PROB_EXITO_BAYA, GASTO_ENERGIA_POCION, PROB_EXITO_POCION, GASTO_ENERGIA_CARAMELO, PROB_EXITO_CARAMELO, AUMENTAR_ATAQUE_FUEGO, AUMENTAR_VIDA_PLANTA, AUMENTAR_VELOCIDAD_AGUA
from random import randint
class Programon(ABC):
    def __init__(self, nombre: str, tipo: str, nivel: int, vida: int, ataque: int, defensa: int, velocidad: int, *args, **kwargs):
        self.nombre = nombre
        self.nivel = nivel
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.experiencia = 0
        
        
    @abstractmethod
    def ganar_batalla(self):
        pass
    
    @abstractmethod
    def aumento_experiencia(self):
        numero = randint(MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA)
        print(f"\nExperiencia Programón [{self.nombre}] era de [{self.experiencia}] y ahora es -> [{self.experiencia + numero}]")
        self.experiencia += numero
        return
    def __repr__(self) -> str:
        return self.nombre
    def __str__(self) -> str:
        return self.nombre
    
    
class ProgramonFuego(Programon):
    tipo = "fuego"
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__nivel = self.nivel
        self.__vida = self.vida
        self.__ataque = self.ataque
        self.__defensa = self.defensa
        self.__velocidad = self.velocidad
        self.__experiencia = self.experiencia

    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, val):
        if 1 <= val <= 100:
            self.__nivel = val
        if val < 1:
            self.__nivel = 1
        if val > 100:
            print(f"El programón {self.nombre} ganó, su nivel pasará a 1")
            self.__nivel = 1
            
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, val):
        if 1 <= val <= 255:
            self.__vida = val
        if val < 1:
            self.__vida = 1
        if val > 255:
            print(f"El programón {self.nombre} tiene una vida superior, pasará a ser 1")
            self.__nivel = 1

    @property
    def ataque(self):
        return self.__ataque
    @ataque.setter
    def ataque(self, val):
        if 5 <= val <= 190:
            self.__ataque = val
        if val < 5:
            self.__ataque = 5
        if val > 190:
            print(f"El programón {self.nombre} tiene un ataque superior, pasará a ser 255")
            self.__ataque = 5

    @property
    def defensa(self):
        return self.__defensa
    @defensa.setter
    def defensa(self, val):
        if 5 <= val <= 250:
            self.__defensa = val
        if val < 5:
            self.__defensa = 5
        if val > 250:
            print(f"El programón {self.nombre} tiene una defensa superior, pasará a ser 250")
            self.__defensa = 250
            
    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self, val):
        if 5 <= val <= 200:
            self.__velocidad = val
        if val < 5:
            self.__velocidad = 5
        if val > 200:
            print(f"El programón {self.nombre} tiene una velocidad superior, pasará a ser 200")
            self.__velocidad = 5
            
    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, val):
        if 0 <= val < 100:
            self.__experiencia = val
        if val < 0:
            self.__experiencia = 0
        if val >= 100:
            self.nivel += 1
            print(f"El programón {self.nombre} tiene 100 de experiencia\n, pasará al siguiente nivel {self.nivel}")
            self.__experiencia = 0
    
        
    def ganar_batalla(self):
        super().ganar_batalla()
        self.ataque += AUMENTAR_ATAQUE_FUEGO
    
    def aumento_experiencia(self):
        return super().aumento_experiencia()
    
        
class ProgramonAgua(Programon):
    tipo = "agua"
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__nivel = self.nivel
        self.__vida = self.vida
        self.__ataque = self.ataque
        self.__defensa = self.defensa
        self.__velocidad = self.velocidad
        self.__experiencia = self.experiencia

    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, val):
        if 1 <= val <= 100:
            self.__nivel = val
        if val < 1:
            self.__nivel = 1
        if val > 100:
            print(f"El programón {self.nombre} ganó, su nivel pasará a 1")
            self.__nivel = 1
            
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, val):
        if 1 <= val <= 255:
            self.__vida = val
        if val < 1:
            self.__vida = 1
        if val > 255:
            print(f"El programón {self.nombre} tiene una vida superior, pasará a ser 1")
            self.__nivel = 1

    @property
    def ataque(self):
        return self.__ataque
    @ataque.setter
    def ataque(self, val):
        if 5 <= val <= 190:
            self.__ataque = val
        if val < 5:
            self.__ataque = 5
        if val > 190:
            print(f"El programón {self.nombre} tiene un ataque superior, pasará a ser 255")
            self.__ataque = 5

    @property
    def defensa(self):
        return self.__defensa
    @defensa.setter
    def defensa(self, val):
        if 5 <= val <= 250:
            self.__defensa = val
        if val < 5:
            self.__defensa = 5
        if val > 250:
            print(f"El programón {self.nombre} tiene una defensa superior, pasará a ser 250")
            self.__defensa = 250
            
    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self, val):
        if 5 <= val <= 200:
            self.__velocidad = val
        if val < 5:
            self.__velocidad = 5
        if val > 200:
            print(f"El programón {self.nombre} tiene una velocidad superior, pasará a ser 200")
            self.__velocidad = 5
            
    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, val):
        if 0 <= val < 100:
            self.__experiencia = val
        if val < 0:
            self.__experiencia = 0
        if val >= 100:
            print(f"El programón {self.nombre} tiene 100 de experiencia\n, pasará al siguiente nivel {self.nivel}")
            self.nivel += 1
            self.__experiencia = 0
    

        
    def ganar_batalla(self):
        super().ganar_batalla()
        self.velocidad += AUMENTAR_VELOCIDAD_AGUA

    def aumento_experiencia(self):
        return super().aumento_experiencia()

class ProgramonPlanta(Programon):
    tipo = "planta"
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__nivel = self.nivel
        self.__vida = self.vida
        self.__ataque = self.ataque
        self.__defensa = self.defensa
        self.__velocidad = self.velocidad
        self.__experiencia = self.experiencia

    @property
    def nivel(self):
        return self.__nivel
    @nivel.setter
    def nivel(self, val):
        if 1 <= val <= 100:
            self.__nivel = val
        if val < 1:
            self.__nivel = 1
        if val > 100:
            print(f"El programón {self.nombre} ganó, su nivel pasará a 1")
            self.__nivel = 1
            
    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, val):
        if 1 <= val <= 255:
            self.__vida = val
        if val < 1:
            self.__vida = 1
        if val > 255:
            print(f"El programón {self.nombre} tiene una vida superior, pasará a ser 1")
            self.__nivel = 1

    @property
    def ataque(self):
        return self.__ataque
    @ataque.setter
    def ataque(self, val):
        if 5 <= val <= 190:
            self.__ataque = val
        if val < 5:
            self.__ataque = 5
        if val > 190:
            print(f"El programón {self.nombre} tiene un ataque superior, pasará a ser 255")
            self.__ataque = 5

    @property
    def defensa(self):
        return self.__defensa
    @defensa.setter
    def defensa(self, val):
        if 5 <= val <= 250:
            self.__defensa = val
        if val < 5:
            self.__defensa = 5
        if val > 250:
            print(f"El programón {self.nombre} tiene una defensa superior, pasará a ser 250")
            self.__defensa = 250
            
    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self, val):
        if 5 <= val <= 200:
            self.__velocidad = val
        if val < 5:
            self.__velocidad = 5
        if val > 200:
            print(f"El programón {self.nombre} tiene una velocidad superior, pasará a ser 200")
            self.__velocidad = 5
            
    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, val):
        if 0 <= val < 100:
            self.__experiencia = val
        if val < 0:
            self.__experiencia = 0
        if val >= 100:
            print(f"El programón {self.nombre} tiene 100 de experiencia\n, pasará al siguiente nivel {self.nivel}")
            self.nivel += 1
            self.__experiencia = 0
    
       
    def ganar_batalla(self):
        super().ganar_batalla()
        self.vida += AUMENTAR_VIDA_PLANTA
        
    def aumento_experiencia(self):
        return super().aumento_experiencia()

    
