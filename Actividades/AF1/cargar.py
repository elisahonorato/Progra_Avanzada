# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
from collections import namedtuple
import readline


def cargar_platos(ruta_archivo: str) -> list:
    mis_platos = []
    Plato = namedtuple("Plato",("nombre", "categoría", "tiempo", "precio", "ingredientes"))
    with open(ruta_archivo, "r", encoding = "utf-8") as platos:
        for plato in platos:
            plato = plato.strip().split(",")
            plato[2], plato [3] = int(plato[2]), int(plato[3])
            ingredientes = plato[4].split(";")
            ingredientes_unicos = set(ingredientes)
            mis_platos.append(Plato(plato[0], plato[1], plato[2], plato[3], ingredientes_unicos))
    return mis_platos


# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    pass
cargar_platos("platos.csv")