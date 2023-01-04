"""
Modulo contiene la clase Logica del servidor
"""
from collections import deque
from os.path import join
from random import choices, sample

from cartas import get_penguins
from utils import data_json


class Logica:
    def __init__(self, parent):
        # Esto permite ejecutar funciones de la clase Servidor
        self.parent = parent
        self.usuarios = []
        self.cartas_ronda = []
        self.jugando = []
        self.lleno = False

    def get_id(self, id):
        """
        busca el usuario correspondiente a un id entregado
        """
        for usuario in self.usuarios:
            if usuario.id_cliente == id:
                return usuario

    def get_nombre(self, nombre):
        """
        busca el usuario correspondiente a un nombre entregado
        """
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario

    def validar_login(self, nombre, socket_cliente):
        print(
            f"cliente {self.parent.id_cliente - 1} ingresa nombre de usuario: {nombre}".center(
                82, " "
            )
        )
        if (
            1 <= len(nombre) <= 10
            and nombre.isalnum()
            and nombre not in [usuario.nombre for usuario in self.usuarios]
        ):
            print(f"Usuario {nombre} Aceptado".center(82, " "))
            usuario = Usuario(nombre, self.parent.id_cliente - 1)
            self.usuarios.append(usuario)
            usuario.index = self.usuarios.index(usuario)
            usuario.mazo = self.get_assets(get_penguins())
            self.get_oponente(usuario.id_cliente)
            if usuario.oponente is not None:
                self.jugando.append(usuario)

            # nombre_usuario Aceptado
            if usuario.oponente is None:
                return [
                    {
                        "comando": "respuesta_validacion_login",
                        "respuesta": {
                            "nombre_usuario": usuario.nombre,
                            "estado": "aceptado",
                            "espera": self.lleno,
                        },
                        "user_id": usuario.id_cliente,
                    }
                    
                ]
            if usuario.oponente is not None:
                return [
                    {
                        "comando": "respuesta_validacion_login",
                        "respuesta": {
                            "nombre_usuario": usuario.nombre,
                            "estado": "aceptado",
                            "espera": self.lleno,
                        },
                        "user_id": usuario.id_cliente,
                    },
                    {
                        "comando": "respuesta_validacion_oponente",
                        "respuesta": {"oponente": usuario.oponente.nombre},
                        "user_id": usuario.id_cliente,
                    },
                    {
                        "comando": "respuesta_validacion_oponente",
                        "respuesta": {"oponente": usuario.nombre},
                        "user_id": usuario.oponente.id_cliente,
                    },
                ]

        # nombre_usuario No Aceptado
        print(f"Usuario {nombre} No Aceptado".center(82, " "))
        return [
            {
                "comando": "respuesta_validacion_login",
                "respuesta": {"estado": "rechazado"},
                "user_id": self.parent.id_cliente - 1,
            }
        ]

    def get_oponente(self, id):
        usuario = self.get_id(id)
        oponente = self.usuarios[(usuario.index) - 1]
        if usuario:
            if usuario.index == 0 or not oponente.disponible:
                print(
                    f"{usuario.nombre} ingresa en la sala de espera...".center(82, " ")
                )
            elif oponente.disponible and oponente.id_cliente != usuario.id_cliente:
                print("")
                print(
                    f"Comienza juego entre {usuario.nombre} y {oponente.nombre}".center(
                        82, " "
                    )
                )
                oponente.disponible = False
                usuario.disponible = False
                oponente.oponente = usuario
                usuario.oponente = oponente
                return usuario.oponente
            return None

    def get_assets(self, dict):
        contador = 0
        lista_cartas = []
        for numero_carta in range(15):
            carta = dict[str(numero_carta)]
            lista_cartas.append(
                Carta(
                    id=numero_carta,
                    elemento=carta["elemento"],
                    puntos=carta["puntos"],
                    color=carta["color"],
                )
            )
            contador += 1
        return lista_cartas

    def get_baraja(self, nombre_usuario, numeros):
        usuario = None
        for usuarios in self.usuarios:
            if usuarios.nombre == nombre_usuario:
                usuario = usuarios
        if usuario is not None:
            baraja = []
            for numero_carta in numeros:
                baraja.append(usuario.mazo[numero_carta].asset)
            usuario.baraja = baraja
            return {
                "comando": "respuesta_actualizar_baraja",
                "respuesta": {"baraja": usuario.baraja},
                "user_id": usuario.id_cliente,
            }

    def get_ganador_juego(self, usuario):
        ganador = None
        respuesta = None

        if len(set(carta.color for carta in usuario.cartas_ganadoras)) == 3:
            if len(set(carta.elemento for carta in usuario.cartas_ganadoras)) == 3:
                ganador = usuario
        elif len(set(carta.color for carta in usuario.oponente.cartas_ganadoras)) == 3:
            if len(set(carta.elemento for carta in usuario.oponente.cartas_ganadoras)) == 3:
                ganador = usuario.oponente
        if ganador is not None:
            mensaje = f"{ganador.nombre} ha ganado la jugada contra {ganador.oponente.nombre}"
            print("|" + mensaje.center(80, "-") + "|")
            respuesta = [
                {
                    "comando": "respuesta_fin",
                    "respuesta": {"resultado_juego": "ganador"},
                    "user_id": ganador.id_cliente,
                },
                {
                    "comando": "respuesta_fin",
                    "respuesta": {"resultado_juego": "perdedor"},
                    "user_id": ganador.oponente.id_cliente,
                },

            ]
        return respuesta

    def get_ganador_partida(self):
        ganador = None
        ganador_juego = None
        if len(self.cartas_ronda) == 2:
            usuario_1 = self.get_id(self.cartas_ronda[0][0])
            carta_1 = self.cartas_ronda[0][1]
            usuario_2 = self.get_id(self.cartas_ronda[1][0])
            carta_2 = self.cartas_ronda[1][1]
            if carta_1.elemento == carta_2.elemento:
                if carta_1.puntos > carta_2.puntos:
                    ganador, carta_ganadora = usuario_1, carta_1
                ganador, carta_ganadora = usuario_2, carta_2
            elif carta_1.elemento == "fuego" and carta_2.elemento == "agua":
                ganador, carta_ganadora = usuario_2, carta_2
            elif carta_1.elemento == "fuego" and carta_2.elemento == "nieve":
                ganador, carta_ganadora = usuario_1, carta_1
            elif carta_1.elemento == "nieve" and carta_2.elemento == "agua":
                ganador, carta_ganadora = usuario_1, carta_1
            elif carta_1.elemento == "nieve" and carta_2.elemento == "fuego":
                ganador, carta_ganadora = usuario_2, carta_2
            elif carta_1.elemento == "agua" and carta_2.elemento == "fuego":
                ganador, carta_ganadora = usuario_1, carta_1
            elif carta_1.elemento == "agua" and carta_2.elemento == "nieve":
                ganador, carta_ganadora = usuario_2, carta_2
            self.cartas_ronda = []
            if ganador is not None:
                print(f"{ganador.nombre} gana la partida".center(82, " "))
                print("")
                ganador.fichas.append(carta_ganadora.asset_ficha)
                ganador.cartas_ganadoras.append(carta_ganadora)
                respuesta = {
                    "comando": "respuesta_mostrar_ganador",
                    "respuesta": {"cartas_ganadoras": ganador.fichas},
                    "user_id": ganador.id_cliente,
                }
                return respuesta
        return None
    
    def validar_juego(self, usuario):
        if usuario not in self.jugando and len(self.jugando) != 2:
            respuesta = [
                {
                    "comando": "respuesta_fin",
                    "respuesta": {"resultado_juego": "ganador"},
                    "user_id": usuario.id_cliente,
                }]
            self.jugando = []
            self.lleno = False
            return respuesta


    def procesar_ronda(self, asset_carta, id):
        """
        Recibe carta enviada por el usuario, y emite una respuesta; la carta a mostrar y también si ganó la ronda
        """
        usuario = self.get_id(id)
        if usuario.oponente in self.usuarios:
            self.lleno = True
            carta_reemplazante = usuario.mazo[0]
            for cartas in usuario.mazo:
                if cartas.asset == asset_carta:
                    carta_lanzada = cartas
                    self.cartas_ronda.append([id, carta_lanzada])
                    print(
                        f"Usuario {usuario.nombre} lanza carta de tipo {carta_lanzada.elemento}".center(
                            82, " "
                        )
                    )
                    usuario.puntaje += carta_lanzada.puntos
                    respuesta = [
                        self.get_baraja(
                            usuario.nombre,
                            sample(range(0, 15), data_json("BARAJA_PANTALLA")),
                        ),
                        {
                            "comando": "respuesta_mostrar_carta",
                            "respuesta": {
                                "carta_mostrar": carta_lanzada.asset,
                                "carta_reemplazante": carta_reemplazante.asset,
                                "elemento": carta_lanzada.elemento,
                                "puntos": carta_lanzada.puntos,
                            },
                            "user_id": usuario.oponente.id_cliente,
                        },
                    ]
                    ganador_partida = self.get_ganador_partida()
                    if ganador_partida is not None:
                        respuesta.append(ganador_partida)
                    ganador_juego = self.get_ganador_juego(usuario)
                    if ganador_juego is not None:
                        for respuestas in ganador_juego:
                            respuesta.append(respuestas)

                    return respuesta

    def procesar_mensaje(self, mensaje, socket_cliente):
        """
        Procesa un mensaje recibido desde el cliente
        """
        try:
            comando = mensaje["comando"]
        except KeyError:
            return {}
        if comando == "validar_login":
            respuesta = self.validar_login(
                mensaje["nombre_usuario"],
                socket_cliente,
            )
        if comando == "enviar_inicio":
            respuesta = [
                self.get_baraja(
                    mensaje["nombre_usuario"],
                    sample(range(0, 15), data_json("BARAJA_PANTALLA")),
                )
            ]
        if comando == "enviar_ronda":
            respuesta = self.procesar_ronda(mensaje["carta"], mensaje["user_id"])
            is_juego_valido = self.validar_juego(self.get_id(mensaje["user_id"]))
            if is_juego_valido is False:
                respuesta.append(is_juego_valido)
                
        return respuesta

    def eliminar_nombre(self, id):
        """
        Elimina el nombre del usuario del diccionario
        """
        self.usuarios.remove(self.get_id(id))


class Usuario:
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.index = None
        self.disponible = True
        self.oponente = None
        self.puntaje = 0
        self.mazo = []
        self.baraja = []
        self.fichas = []
        self.cartas_ganadoras = []

    def __repr__(self) -> str:
        return f"{self.nombre}"


class Carta:
    def __init__(self, id: int, elemento: str, puntos: int, color: str):
        self.id = id
        self.elemento = elemento
        self.puntos = int(puntos)
        self.color = color
        self.asset = f"sprites/cartas/{color}_{elemento}_{puntos}.png"
        self.asset_ficha = f"sprites/elementos/fichas/{elemento}_{color}.png"
