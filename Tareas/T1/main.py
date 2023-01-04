from __future__ import annotations
from entidades import Entrenador, Objeto, Programon, ProgramonAgua, ProgramonFuego, ProgramonPlanta, Baya, Pocion, Caramelo
from abc import ABC, abstractmethod
from funciones_generales.path import Path
from funciones_generales.input import get_input
from random import choices, randint, sample

class Menu(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def ejecutar_menu(self):
        print(f"\n*** {self.nombre} ***")
        print("--------------------------------------------------")

    @abstractmethod
    def volver(self):
        return 'Volver'

    @abstractmethod
    def salir(self):
        return 'Salir'


class MenuUtilizarObjeto(Menu):
    def __init__(self, liga: LigaProgramon, entrenador: Entrenador, **kwargs):
        self.liga = liga
        self.entrenador = entrenador
        super().__init__(nombre="Menu Utilizar Objeto", **kwargs)

    def ejecutar_menu(self, respuesta):
        while respuesta != "Salir":
            super().ejecutar_menu()
            for index, objeto in enumerate(self.entrenador.objetos):
                print(f"[{index + 1}] {str(objeto)}")
            print(f"[{len(self.entrenador.objetos)+1}] Volver")
            print(f"[{len(self.entrenador.objetos)+2}] Salir")
            respuesta = get_input(len(self.entrenador.objetos) + 2)
            if respuesta == "Volver":
                return self.volver()
            elif respuesta == "Salir":
                return self.salir()
            else:
                objeto = self.entrenador.objetos[respuesta - 1]
            for index, programon in enumerate(self.entrenador.programones):
                print(
                    f"[{index + 1}] {str(programon)}")
            print(f"[{len(self.entrenador.programones)+1}] Volver")
            print(f"[{len(self.entrenador.programones)+2}] Salir")
            respuesta = get_input(len(self.entrenador.programones)+2)
            if respuesta not in ("Salir", "Volver"):
                programon = self.entrenador.programones[respuesta-1]
                respuesta = objeto.aplicar_objeto(programon)
                self.entrenador.objetos.remove(objeto)
            elif respuesta == "Salir":
                return self.salir()
            elif respuesta == "Volver":
                return self.volver()
        return respuesta

    def volver(self):
        return super().volver()

    def salir(self):
        return super().salir()


class MenuCrearObjeto(Menu):
    def __init__(self, liga: LigaProgramon, entrenador: Entrenador, **kwargs):
        self.liga = liga
        self.entrenador = entrenador
        super().__init__(nombre="Menu Crear Objeto", **kwargs)

    def ejecutar_menu(self, respuesta):
        while respuesta != "Salir":
            super().ejecutar_menu()
            print(
                "[1] Baya\n[2] Poción\n[3] Caramelo\n"
                "[4] Volver\n[5] Salir\n")
            respuesta = get_input(5)
            if respuesta == "Volver":
                return self.volver()
            elif respuesta == "Salir":
                return self.salir()
            else:
                respuesta = self.entrenador.crear_objetos(
                    respuesta, self.liga.objetos)
        return respuesta

    def volver(self):
        return super().volver()

    def salir(self):
        return super().salir()


class MenuEntrenamiento(Menu):
    def __init__(self, liga: LigaProgramon, entrenador: Entrenador, **kwargs):
        self.liga = liga
        self.entrenador = entrenador
        super().__init__(nombre="Menu Entrenamiento", **kwargs)

    def ejecutar_menu(self, respuesta):
        while respuesta != "Salir":
            super().ejecutar_menu()
            for index, programon in enumerate(self.entrenador.programones):
                print(f"[{index + 1}] {str(programon)}")
            print(f"[{len(self.entrenador.programones)+1}] Volver")
            print(f"[{len(self.entrenador.programones)+2}] Salir")
            respuesta = get_input(len(self.entrenador.programones) + 2)
            if respuesta == "Volver":
                return self.volver()
            elif respuesta == "Salir":
                return self.salir()
            else:
                respuesta = self.entrenador.entrenamiento(respuesta)
        return respuesta

    def volver(self):
        return super().volver()

    def salir(self):
        return super().salir()


class MenuRonda(Menu):
    def __init__(self, liga: LigaProgramon, entrenador: Entrenador, **kwargs):
        self.liga = liga
        self.entrenador = entrenador
        super().__init__(nombre="Elige a tu Luchador", **kwargs)

    def ejecutar_menu(self, respuesta):
        respuesta = ""
        while respuesta != "Salir":
            super().ejecutar_menu()
            for index, programon in enumerate(self.entrenador.programones):
                print(f"[{index + 1}] {str(programon)}")
            print(f"[{len(self.entrenador.programones)+1}] Volver")
            print(f"[{len(self.entrenador.programones)+2}] Salir")
            respuesta = get_input(len(self.entrenador.programones) + 2)
            return respuesta

    def volver(self):
        return super().volver()

    def salir(self):
        return super().salir()


class MenuEntrenador(Menu):
    def __init__(self, liga: LigaProgramon, entrenador: Entrenador, **kwargs):
        self.liga = liga
        self.entrenador = entrenador
        super().__init__(nombre="Menu Entrenador", **kwargs)

    def ejecutar_menu(self, respuesta):
        while respuesta != "Salir":
            super().ejecutar_menu()
            print(
                "[1] Entrenamiento\n[2] Simular ronda\n[3] Resumen campeonato\n"
                "[4] Crear objetos\n[5] Utilizar objeto\n[6] Estado entrenador\n[7] Volver"
                "\n[8] Salir")
            handler = {
                1: MenuEntrenamiento(self.liga, self.entrenador).ejecutar_menu,
                2: self.liga.simular_ronda,
                3: self.liga.resumen_campeonato,
                4: MenuCrearObjeto(self.liga, self.entrenador).ejecutar_menu,
                5: MenuUtilizarObjeto(self.liga, self.entrenador).ejecutar_menu,
                6: self.entrenador.estado_entrenador,
            }
            respuesta = get_input(8)
            args = [respuesta]
            if respuesta == 2:
                args = [self.entrenador]
            if respuesta == 6:
                resultado = handler[6](*args)
                if resultado == 1:
                    return self.volver()
                if resultado == 2:
                    return self.salir()
            if respuesta == "Volver":
                return self.volver()
            if respuesta == "Salir":
                return self.salir()
            else:
                respuesta = handler[respuesta](*args)
        return respuesta

    def volver(self):
        return super().volver()

    def salir(self):
        return super().salir()


class MenuInicio(Menu):
    def __init__(self, liga: LigaProgramon, **kwargs):
        self.liga = liga
        super().__init__(nombre="Menu Inicio", **kwargs)

    def volver(self):
        return super().volver()

    def salir(self):
        return super().salir()

    def ejecutar_menu(self, respuesta):
        respuesta = ""
        while respuesta != "Salir":
            super().ejecutar_menu()
            for index, entrenador in enumerate(self.liga.entrenadores):
                print(
                    f"[{index + 1}] {entrenador.nombre}: {', '.join((str(programon)) for programon in entrenador.programones)}")
            print(f"[{len(self.liga.entrenadores)+1}] Salir")
            respuesta = get_input(len(self.liga.entrenadores) + 2)
            if respuesta == "Salir":
                return self.salir()
            elif respuesta == "Volver":
                return self.salir()
            else:
                MenuEntrenador(
                    self.liga, self.liga.entrenadores[respuesta-1]).ejecutar_menu(respuesta)
        return respuesta


class LigaProgramon:
    def __init__(self):
        self.objetos = self.leer_objetos()
        self.programones = self.leer_programones()
        self.entrenadores = self.leer_entrenadores()
        self.perdedores = []
        self.ronda_actual = 0
        self.campeon = None
        self.rondas = [[entrenador for entrenador in self.entrenadores]]

    def resumen_campeonato(self, *args):
        print("Resumen Campeonato")
        print(
            "----------------------------------------------------------------------------")
        print(
            f"Participantes :{([(entrenador.nombre) for entrenador in self.rondas[self.ronda_actual]])}")
        print(f"Ronda Actual: {self.ronda_actual}")
        print(
            f"Entrenadores que siguen en la competencia: {([(entrenador.nombre) for entrenador in self.entrenadores if entrenador not in self.perdedores])} ")

    def simular_ronda(self, entrenador_actual):
        menu = MenuRonda(self, entrenador_actual)
        respuesta = menu.ejecutar_menu("")

        if respuesta != "Salir" or entrenador_actual not in self.perdedores:
            self.ronda_actual += 1
            print(f"Ronda {self.ronda_actual}")
            print(
                "----------------------------------------------------------------------------")
            pares_entrenadores = []
            elegidos = []
            self.rondas.append([entrenador for entrenador in self.entrenadores])
            while len(pares_entrenadores) < len(self.entrenadores) // 2:
                par = sample(list(
                    entrenador for entrenador in self.entrenadores if entrenador not in elegidos), 2)
                elegidos += par
                pares_entrenadores.append(par)
            for par in pares_entrenadores:
                perdedor = self.luchar(par)
                if perdedor == entrenador_actual:
                    print(f"Perdiste, {entrenador_actual}")
                    return "Salir"
                self.perdedores.append(perdedor)
                self.entrenadores.remove(perdedor)
            if len(self.entrenadores) == 1:
                self.campeon = entrenador_actual
                respuesta = "Salir"
        return respuesta

    def luchar(self, par):
        programon_1 = par[0].elegir_programon_random()
        programon_2 = par[1].elegir_programon_random()
        print(f"{par[0].nombre} usando al programón {programon_1}, se enfrenta a {par[1].nombre} usando al programón {programon_2}")
        ventaja_tipo_1 = 0
        ventaja_tipo_2 = 0
        if programon_1.tipo != programon_2.tipo:
            if programon_1.tipo == "planta":
                if programon_2.tipo in "fuego, agua":
                    ventaja_tipo_1 = -1
                    ventaja_tipo_2 = 1
            elif programon_1.tipo == "fuego":
                if programon_2.tipo == "planta":
                    ventaja_tipo_1 = 1
                    ventaja_tipo_2 = -1
                elif programon_2.tipo == "agua":
                    ventaja_tipo_1 = -1
                    ventaja_tipo_2 = -1
            elif programon_1.tipo == "agua":
                ventaja_tipo_1 = 1
                ventaja_tipo_2 = -1
        puntaje_programon1 = max(0,((programon_1.vida * 0.2) + (programon_1.nivel * 0.3) + (programon_1.ataque * 0.15) + (programon_1.defensa * 0.15) + (programon_1.velocidad * 0.2) + (ventaja_tipo_1 * 40)))
        puntaje_programon2 = max(0,((programon_2.vida * 0.2) + (programon_2.nivel * 0.3) + (programon_2.ataque * 0.15) + (programon_2.defensa * 0.15) + (programon_2.velocidad * 0.2) + (ventaja_tipo_2 * 40)))
        par[0].energia = 0
        par[1].energia = 0
        if puntaje_programon1 < puntaje_programon2:
            print(f"{par[1]} ha ganado la batalla")
            programon_1.ganar_batalla()
            return par[0]
        elif puntaje_programon1 > puntaje_programon2:
            print(f"{par[0]} ha ganado la batalla")
            programon_2.ganar_batalla()
            return par[1]
        elif puntaje_programon1 == puntaje_programon2:
            print("Los entrenadores han empatado, eligiremos uno al azar")
            numero_ganador = randint (0,1)
            entrenador = par[numero_ganador]
            entrenador.programon_random.ganar_batalla()
            par.remove(entrenador)
            return par[0]

    def leer_entrenadores(self) -> list:
        with open(Path.path_join(self, "entrenadores.csv"), "r", encoding="utf-8") as archivo:
            lista_entrenadores = []
            next(archivo)
            for entrenador in archivo:
                list = entrenador.split(",")
                programones_entrenador = []
                nombres_programones = list[1].split(";")
                for nombre in nombres_programones:
                    programon = self.programones[nombre]
                    programones_entrenador.append(programon)
                lista_entrenadores.append(Entrenador(
                    nombre=list[0], energia=list[2], programones=programones_entrenador, objetos=self.leer_objetos_entrenadores(list[3].strip().split(";"))))
            return lista_entrenadores

    def leer_programones(self) -> dict:
        with open(Path.path_join(self, "programones.csv"), "r", encoding="utf-8") as archivo:
            lista_programones = {}
            next(archivo)
            for programon in archivo:
                list = programon.split(",")
                if list[1] == "fuego":
                    programon = {list[0]: ProgramonFuego(
                        nombre=list[0], tipo="Fuego", nivel=int(list[2]), vida=int(list[3]), ataque=int(list[4]), defensa=int(list[5]), velocidad=int(list[6]))}
                elif list[1] == "agua":
                    programon = {list[0]: ProgramonAgua(
                        nombre=list[0], tipo="Agua", nivel=int(list[2]), vida=int(list[3]), ataque=int(list[4]), defensa=int(list[5]), velocidad=int(list[6]))}
                elif list[1] == "planta":
                    programon = {list[0]: ProgramonPlanta(
                        nombre=list[0], tipo="Planta", nivel=int(list[2]), vida=int(list[3]), ataque=int(list[4]), defensa=int(list[5]), velocidad=int(list[6]))}
                lista_programones.update(programon)
            return lista_programones

    def leer_objetos_entrenadores(self, lista) -> list:
        lista_objetos = []
        for nombre_objeto in lista:
            if nombre_objeto in (self.objetos["baya"]):
                objeto = Baya(nombre=nombre_objeto)
            elif nombre_objeto in (self.objetos["pocion"]):
                objeto = Pocion(nombre=nombre_objeto)
            elif nombre_objeto in (self.objetos["caramelo"]):
                objeto = Caramelo(nombre=nombre_objeto)
            lista_objetos.append(objeto)
        return lista_objetos

    def leer_objetos(self) -> dict:
        with open(Path.path_join(self, "objetos.csv"), "r", encoding="utf-8") as archivo:
            next(archivo)
            lista_baya = []
            lista_pocion = []
            lista_caramelo = []
            for objeto in archivo:
                list = objeto.strip().split(",")
                if "baya" in list:
                    if list[1] == "baya":
                        lista_baya.append(list[0])
                    else:
                        lista_baya.append(list[1])
                elif "pocion" in list:
                    if list[1] == "pocion":
                        lista_pocion.append(list[0])
                    else:
                        lista_pocion.append(list[1])
                elif "caramelo" in list:
                    if list[1] == "caramelo":
                        lista_caramelo.append(list[0])
                    else:
                        lista_caramelo.append(list[1])
            lista_objetos = {"baya": lista_baya,
                             "pocion": lista_pocion, "caramelo": lista_caramelo}
            return lista_objetos

    def run(self):
        print("\n¡Hola, bienvenid@ a DCCampeonato!")
        respuesta = ""
        menu = MenuInicio(self)
        respuesta = menu.ejecutar_menu(respuesta)
        return respuesta

if __name__ == "__main__":
    liga = LigaProgramon()
    liga.run()
