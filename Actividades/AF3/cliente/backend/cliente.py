"""
Modulo contiene implementación principal del cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject
import socket
import json
from threading import Thread
from backend.interfaz import Interfaz


class Cliente(QObject):
    senal_mostrar_ventana_carga = pyqtSignal()
    senal_manejar_mensaje = pyqtSignal(dict)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.interfaz = Interfaz()
        self.iniciar_cliente()

    def iniciar_cliente(self):
        """
        Se encarga de iniciar el cliente y conectar el socket
        """
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar()
            self.senal_mostrar_ventana_carga.emit()

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
        # TODO: Completado por estudiante
        while self.conectado:
            try:
                if self.recibir_mensaje():
                    self.interfaz.manejar_mensaje()
            except ConnectionError:
                print("no se pudo conectar")
        

        pass

    def recibir_mensaje(self):
        largo_archivo = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        datos = bytearray()
        bytes_leidos = 0
        print(f"OK. Ahora sé que debe recibido {largo_archivo} bytes")
        # Ahora leemos el archivo por chunks, de máximo 4096 bytes.
        while len(datos) < largo_archivo:
        # El último recv será probablemente más chico que 4096
            bytes_leer = min(64, largo_archivo - len(datos))
            datos_recibidos = self.socket_cliente.recv(bytes_leer)
            # Recordemos que el método recv, entrega una cantidad máxima, pero no nos asegura que nos 
            # entregue los 4096 bytes. Es por esto, que la cantidad de bytes que hemos recibido en
            # total, se deben ver siempre en función de lo que retornó el método recv, y no lo que
            # le entregamos como parámetro
            bytes_leidos += len(datos_recibidos)
            print(f"He recibido {len(datos_recibidos)} bytes en el último recv. Van {bytes_leidos} en total.")
            datos.extend(datos_recibidos)
            print(f"¡Listo! He recibido {len(datos)} bytes")
            return self.decodificar_mensaje(datos)


    def enviar(self, mensaje):
        """
        Envía un mensaje a un cliente.
        """
        # TODO: Completado por estudiante
        pass

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        try:
            mensaje = json.loads(mensaje_bytes)
            return mensaje
        except json.JSONDecodeError:
            print("ERROR: No se pudo decodificar el mensaje")
            return {}
