"""
Modulo contiene implementación principal del cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread
from cripto import encriptar, desencriptar


class Cliente(QObject):
    senal_mostrar_ventana_login = pyqtSignal()
    senal_manejar_mensaje = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            # Uso de TCP con (Connect)
            self.socket_cliente.connect((self.host, self.port))
            self.senal_mostrar_ventana_login.emit()
            self.conectado = True
            self.comenzar_a_escuchar()

        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")

    def comenzar_a_escuchar(self):
        """
        Instancia el Thread que escucha los mensajes del servidor
        """
        thread = Thread(target=self.escuchar_servidor, daemon=True)
        thread.start()

    def escuchar_servidor(self):
        """
        Recibe mensajes constantes desde el servidor y responde.
        """
        try:
            while self.conectado:
                mensaje = self.recibir()
                if mensaje:
                    self.senal_manejar_mensaje.emit(mensaje)
                    
        except ConnectionError as e:
            print("ERROR: Servidor desconectado.", e)

    def recibir(self):
        """
        Se encarga de recibir los mensajes del servidor.
        """

        # Recibir largo del mensaje en bytes
        largo_mensaje_bytes = self.socket_cliente.recv(4)

        # Decodificar los primeros 4 bytes que contienen el largo del contenido.
        largo_mensaje = int.from_bytes(largo_mensaje_bytes, byteorder="little")

        # Recibir mensaje
        bytes_mensaje = bytearray()

        while len(bytes_mensaje) < largo_mensaje:
            tamano_chunk = min(largo_mensaje - len(bytes_mensaje), 32)
            bytes_mensaje += self.socket_cliente.recv(tamano_chunk)

        # Decodificar mensaje
        mensaje = self.decodificar_mensaje(desencriptar(bytes_mensaje))
        return mensaje

    def enviar(self, mensaje):
        """
        Envía un mensaje a un servidor.
        """
        # Codificar Mensaje
        bytes_mensaje = self.codificar_mensaje(mensaje)
        bytes_mensaje = encriptar(bytes_mensaje)

        # Codificar numero identificador de cada bloque a bytes
        len_mensaje= len(bytes_mensaje).to_bytes(4, byteorder="big")

        self.socket_cliente.sendall(len_mensaje + bytes_mensaje)

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode("utf-8")
            return mensaje_bytes
        except json.JSONDecodeError:
            print("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}
