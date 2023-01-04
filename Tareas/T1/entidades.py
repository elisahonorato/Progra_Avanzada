from abc import ABC, abstractmethod
from parametros import AUMENTO_DEFENSA, ENERGIA_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA, MAX_AUMENTO_EXPERIENCIA, GASTO_ENERGIA_BAYA, PROB_EXITO_BAYA, GASTO_ENERGIA_POCION, PROB_EXITO_POCION, GASTO_ENERGIA_CARAMELO, PROB_EXITO_CARAMELO, ENERGIA_CREAR_OBJETO
from random import randint, random, choice
from programones import Programon, ProgramonFuego, ProgramonAgua, ProgramonPlanta
from funciones_generales.input import get_input
class Entrenador:
    def __init__(self, nombre: str, energia: int, programones: list, objetos: list):
        self.nombre = nombre
        self.energia = int(energia)
        self.programones = programones
        self.objetos = objetos
        
    def entrenamiento(self, respuesta):
        programon = self.programones[int(respuesta-1)]
        print(programon.nombre)
        print(f"\nEnergía Entrenador [{self.nombre}] era de [{self.energia}] y ahora es -> [{self.energia - ENERGIA_ENTRENAMIENTO}]")
        self.energia = int(self.energia - ENERGIA_ENTRENAMIENTO)
        programon.aumento_experiencia()
        return
    
    def estado_entrenador(self, *args):
        print("*** Estado entrenador **")
        print("-----------------------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Energía: {self.energia}")
        print(f"Objetos: {', '.join((str(objeto)) for objeto in self.objetos)}")
        print("-----------------------------------------------")
        print("Programones")
        print("-----------------------------------------------")
        print("Nombre | Tipo | Nivel | Vida")
        for programon in self.programones:
            print(f"{programon.nombre} {programon.tipo} {programon.nivel} {programon.vida}")
        print("\n[1] Volver")
        print("[2] Salir")
        input= get_input(2)
        return input
    
    @abstractmethod
    def crear_objetos(self, indice, lista_objetos):
        if indice == 1:
            tipo_objeto = "baya"
            clase_objeto = Baya
        elif indice == 2:
            tipo_objeto = "pocion"
            clase_objeto = Pocion
        elif indice == 3:
            tipo_objeto = "caramelo"
            clase_objeto = Caramelo
        if tipo_objeto != " ":
            lista_tipo = lista_objetos[tipo_objeto]
            numero = randint(0, len(lista_tipo)-1)
            objeto = clase_objeto(nombre= lista_tipo[numero], tipo= tipo_objeto)
            probabilidad_random = random()
            if probabilidad_random >= objeto.probabilidad_exito:
                if objeto.costo <= self.energia:
                    print(f"Se ha creado un Objeto {tipo_objeto.capitalize()} llamado: {objeto.nombre}")
                    self.objetos.append(objeto)
                    self.energia -= objeto.costo
                else:
                    print(f"Error creando objeto:\nLa energía para crear, es menor que la mínima\n{self.energia} < {objeto.costo}")
            else: 
                probabilidad_random_format = "{:.3f}".format(probabilidad_random)
                print(f"Error creando objeto:\nLa probabilidad de tu objeto, es menor que la mínima\n{probabilidad_random_format} < {objeto.probabilidad_exito}")
            return 

    
    def elegir_programon_random(self) -> Programon:
        self.programon_random = choice(self.programones)
        return self.programon_random
    
    def __repr__(self) -> str:
        return self.nombre

    
class Objeto(ABC):
    def __init__(self, nombre: str, *args, **kwargs):
        self.nombre = nombre    

    def __str__(self) -> str:
        return self.nombre
        
    @abstractmethod
    def aplicar_objeto(self, programon):
        print(f"Programón beneficiado: {str(programon)}")
        print(f"Objeto utilizado: {self.nombre} (Tipo {repr(self.tipo.capitalize())})")

        
class Baya(Objeto):
    probabilidad_exito = PROB_EXITO_BAYA
    tipo = "baya"
    costo = GASTO_ENERGIA_BAYA

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        numero = randint(1, 10)
        if int(programon.vida) + numero < 255:
            programon.vida += numero
        print(f"Aumento vida: {numero}")
        print(f"La vida subió de {programon.vida - numero} a {programon.vida}")
    
    
class Pocion(Objeto):
    probabilidad_exito = PROB_EXITO_POCION
    tipo = "pocion"
    costo = GASTO_ENERGIA_POCION
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        numero = randint(1, 7)
        if int(programon.ataque) + numero < 190:
            programon.ataque += numero
        print(f"Aumento ataque: {numero}")
        print(f"El ataque subió de {programon.ataque - numero} a {programon.ataque}")


class Caramelo(Baya, Pocion):
    probabilidad_exito = PROB_EXITO_CARAMELO
    tipo = "caramelo"
    costo = GASTO_ENERGIA_CARAMELO
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def aplicar_objeto(self, programon):
        super().aplicar_objeto(programon)
        programon.defensa += AUMENTO_DEFENSA
        print(f"Aumento defensa: {AUMENTO_DEFENSA}")
        print(f"La defensa subió de {programon.defensa - AUMENTO_DEFENSA} a {programon.defensa}")




