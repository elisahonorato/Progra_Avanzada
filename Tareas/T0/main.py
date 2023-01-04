import os
import os.path
from jugar import Tablero
from input import get_input, get_input_abc
from path import Path


class Partida:
    def __init__(self, nombre_usuario):
        self.nombre = nombre_usuario
        self.puntaje = 0
        self.jugadas = 0
        self.tablero = None
        self.path_main = Path.path_main(self)
        self.path_nombre = Path.path_nombre(self, self.nombre)
        
    def menu_jugada(self):
        respuesta = ""
        while respuesta != 0:
            print("\n-- Menú de Juego --")
            print(
                "Para esta jugada, seleccione una opción:\n[1] Descubrir Sector\n"
                "[2] Guardar Partida\n[0] Salir de la Partida"
            )
            handler = {
                1: self.jugar,
                2: self.guardar_partida,
                0: self.salir,
            }
            respuesta = get_input(2)
            resultado = handler[respuesta]()
            if resultado == 'salir':
                break
    
    def jugar(self):
        print('Ingrese la coordenada y: ')
        y = int(get_input(self.tablero.largo-1))
        print('Ingrese la coordenada x: ')
        x = int(get_input_abc(self.tablero.ancho-1))
        result = self.tablero.descubrir_sector(y, x)
        if not result:
            print(
                "Encontraste una bestia Nexus, tu partida ha terminado")
            self.tablero.estado = str("Completo")
            self.tablero.print_celdas()
            return self.salir()
        else:
            self.jugadas += 1
            self.tablero.print_celdas()
            if len(self.tablero.casillas_descubiertas) == self.tablero.libres:
                self.tablero.estado = str("Completo")
                print(f"{self.nombre}, Ganaste!!!")
                return self.salir()

    def crear_partida(self):
        print("Seleccione largo del tablero: ")
        largo_tablero = int(get_input(100))
        if largo_tablero == 0:
            print(f"Debes ingresar un número dentro del rango")
            largo_tablero = int(get_input(100))
        print("Seleccione ancho del tablero: ")
        ancho_tablero = int(get_input(100))
        if ancho_tablero == 0:
            print(f"Debes ingresar un número dentro del rango")
            ancho_tablero = int(get_input(100))
        self.tablero = Tablero(largo_tablero, ancho_tablero)
        self.tablero.crear_tablero()
        self.tablero.print_celdas()
        self.menu_jugada()
        
    
    def guardar_partida(self):
        with open(self.path_nombre, "w", encoding="utf-8") as archivo:
            archivo.write(self.tablero.estado)
            archivo.write('\n')
            archivo.write(self.nombre)
            archivo.write('\n')
            archivo.write(str(self.tablero.calcular_puntaje()))
            archivo.write('\n')
            archivo.write(str(self.tablero.largo))
            archivo.write('\n')
            archivo.write(str(self.tablero.ancho))
            archivo.write('\n')
            archivo.write(self.tablero.guardar_tablero())
        with open(Path.path_añadir(self, "partidas.txt"), "a", encoding="utf-8") as archivo:
            archivo.write(f"{self.nombre},{self.tablero.calcular_puntaje()}")
            archivo.write('\n')
            return 
                
    def cargar_partida(self):
        with open(self.path_nombre, "r", encoding="utf-8") as archivo:
            estado = next(archivo).strip()
            if estado == "Incompleto":
                self.nombre = next(archivo).strip()
                self.puntaje = next(archivo).strip()
                largo_tablero = next(archivo).strip()
                ancho_tablero = next(archivo).strip()
                self.tablero = Tablero(largo_tablero, ancho_tablero)
                for largo in range(int(largo_tablero)):
                    fila = next(archivo).strip('\n')
                    self.tablero.leer_fila(fila, largo)
                self.tablero.print_celdas()
            if estado == "Completo":
                print("No puedes seguir jugando, tu tablero ya terminó")
                return self.salir()
                
                
    def salir(self):
        """
        Esta función retorna al menú de inicio
        """
        print("¿Deseas Guardar?\n[1] Si\n"
              "[0] No")
        respuesta = get_input(1)
        if respuesta == 1:
            self.guardar_partida()
        return 'salir'
            
     

class Star_Avanced:
    def __init__(self):
        self.path_main = Path.path_main(self)

    def menu_inicio(self):
        respuesta = ""
        while respuesta != 0:
            print("\n-- Menú Inicial --")
            print(
                "¿Qué deseas hacer?\n[1] Nueva Partida\n"
                "[2] Cargar Partida Anterior\n[3] Visualizar Ranking"
                "\n[0] Salir"
            )
            respuesta = get_input(3)
            handler = {
                1: self.nueva_partida,
                2: self.partida_anterior,
                3: self.visualizar_ranking,
                0: self.salir,
            }
            handler[respuesta]()
            
    def nueva_partida(self):
        self.crear_carpeta(Path.path_añadir(self, "partidas"))
        nombre = self.get_nombre()
        partida = Partida(nombre)
        print(
            f"Bienvenid@ {partida.nombre}, deberás crear un tablero para iniciar")
        partida.crear_partida()
        if not partida.menu_jugada:
            self.menu_inicio() 
    
    def partida_anterior(self):
        nombre = self.get_nombre()
        if os.path.exists(Path.path_nombre(self, nombre)) == True:
            print(f"Bienvenid@ nuevamente, {nombre}")
            partida = Partida(nombre)
            puede = partida.cargar_partida()
            if puede == 'salir':
                return
            if not partida.menu_jugada():
                self.menu_inicio()
        else:
            print("No hay partidas asociadas a este Usuario")

    def visualizar_ranking(self):
        with open(Path.path_añadir(self, "partidas.txt"), "r", encoding="utf-8") as archivo:
            puntajes = []
            for usuario in archivo:
                x = usuario.split(",")
                puntajes.append([x[0], int(x[1])])
            mejores_puntajes = sorted(puntajes, key=lambda x: x[1], reverse = True)
            self.imprimir_ranking(mejores_puntajes)
    
    def imprimir_ranking(self, lista):
        seleccion = lista[:12]
        print("\n-- Los mejores juegos de Star Avanced de todos los tiempos --")
        contador = 0
        for usuario in seleccion:
            contador +=1
            nombre = usuario[0]
            puntaje = usuario[1]
            numero = contador
            print(f"{numero}. {nombre} ({puntaje} puntos).")
            
    def crear_carpeta(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print('Error creando carpeta en' + path)
            
    def get_nombre(self):
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        return nombre_usuario
            
    def salir(self):
        print("Hasta Pronto!")
        return

if __name__ == "__main__":
    print("\n¡Hola, bienvenid@ a Star Avanced!")
    juego = Star_Avanced()
    juego.menu_inicio()