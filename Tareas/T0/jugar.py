import random
import math
import string
from parametros import POND_PUNT, PROB_BESTIA
from tablero import print_tablero_con_utf8, print_tablero_sin_utf8
from input import get_input


class Celda:
    def __init__(self, posicion_y, posicion_x, info):
        self.y = posicion_y
        self.x = posicion_x
        self.info = info

    def __repr__(self) -> str:
        return self.info
    
    def guardar_string(self):
        return f'{self.x, self.y}: {self.info}'


class Tablero:
    def __init__(self, largo_tablero, ancho_tablero):
        self.largo = int(largo_tablero)
        self.ancho = int(ancho_tablero)
        self.bestias = math.ceil(self.largo * self.ancho * PROB_BESTIA)
        self.libres = int((self.largo * self.ancho) - self.bestias)
        self.casillas = []
        self.casillas_descubiertas = []
        self.estado = str("Incompleto")
        
    def guardar_tablero(self):
        string = ''
        for fila in self.casillas:
            string += ','.join(str(celda.info) for celda in fila)
            string += '\n'
        return string

    def crear_tablero(self):
        for y in range(self.largo):
            self.casillas.append([])
            for x in range(self.ancho):
                self.casillas[y].append(Celda(y, x, ' '))
        posible_casillas = [(y, x) for x in range(self.ancho)
                             for y in range(self.largo)]
        bestias_position = random.sample(posible_casillas, self.bestias)
        for y, x in bestias_position:
            self.casillas[y][x].info = "N"
            
    def leer_fila(self, fila, largo):
        nueva_fila = []
        info = fila.split(",")
        for ancho in range(len(info)):
            nueva_fila.append(Celda(largo, ancho, str(info[ancho])))
        self.casillas.append(nueva_fila)
    

    def print_celdas(self):
        print("\nEstado Actual del Tablero:\n")
        lista_casillas = [[celda.info for celda in row]
            for row in self.casillas]
        print_tablero_con_utf8(lista_casillas)

    def descubrir_sector(self, y, x):
         y = int(y)
         x = int(x)
         if self.casillas[y][x].info == 'N':
             return False
         self.casillas_descubiertas.append(self.casillas[y][x])
         self.contar_bestias(y, x)
         return True

    def contar_bestias(self, y, x):
        adyacentes = [
            (1, -1),
            (1, 0),
            (1, 1),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]
        contador = 0
        for a, b in adyacentes:
            try:
                if y + a < 0 or x + b < 0:
                    pass
                elif self.casillas[y + a][x + b].info == 'N':
                    contador += 1
            except IndexError:
                pass
        self.casillas[y][x].info = contador

    def calcular_puntaje(self):
        puntaje = self.bestias * len(self.casillas_descubiertas) * POND_PUNT
        return puntaje
