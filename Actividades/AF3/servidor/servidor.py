"""
Modulo contiene la implementación principal del servidor
"""
import json
import socket
import threading
from logica import Logica


class Servidor:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_servidor = None
        self.logica = Logica(self)
        self.id_cliente = 0
        self.log("".center(80, "-"))
        self.log("Inicializando servidor...")
        self.sockets = {}
        self.iniciar_servidor()

    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.conectado = False

        try:
            self.socket_servidor.bind((self.host, self.port))
            self.socket_servidor.listen()
            data = self.socket_servidor.recv(4096)
            print(data.decode('utf-8'))
            self.log(self.host, self.port)
            self.socket_servidor.conectado = True
            self.comenzar_a_aceptar()

        except ConnectionError as e:
            # ConnectionError es la clase base BrokenPipeError, ConnectionAbortedError,
            # ConnectionRefusedError y ConnectionResetError
            print("Ocurrió un error.")
        finally:
            # ¡No olvidemos cerrar la conexión!
            self.socket_servidor.close()
    def comenzar_a_aceptar(self):
        """
        Crea y comienza el thread encargado de aceptar clientes
        """
        thread = threading.Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()

    def aceptar_clientes(self):
        """
        Es arrancado como thread para de aceptar clientes, este se ejecuta
        siempre que se este conectado y acepta el socket del servidor. Luego
        se crea y comienza a escuchar al cliente. para finalmente aumentar en 1
        el id_cliente.
        """
        # TODO: Completado por estudiante
        while self.socket_servidor.conectado:
            try:
                socket_cliente, address = self.socket_servidor.accept()
                socket_cliente.sendall("Gracias por conectarte\n".encode("utf-8"))

            except ConnectionError as e:
                print("Ocurrió un error.")
                self.socket_servidor.conectado = False

            finally:
                id_cliente = address
                thread = threading.Thread(target=self.escuchar_cliente(id_cliente), daemon=True)
                thread.start()

        
    def escuchar_cliente(self, id_cliente, socket_cliente):
        """
        Ciclo encargado de escuchar a cada cliente de forma individual, esta
        funcion se ejecuta siempre que el servidor este conectado, recibe el
        socket del cliente y si hay un mensaje, lo procesa con la funcion
        instanciada en la logica.
        """
        while socket_cliente:
        # TODO: Completado por estudiante
            mensaje = self.recibir_mensaje()
            if mensaje != '':
                try:
                    self.log(f"Comenzando a escuchar al cliente {id_cliente}...")
                    if self.logica.procesar_mensaje() != {}:
                        self.enviar_mensaje()

                except ConnectionError as e:
                    self.eliminar_cliente(id_cliente)
                    print("Ocurrió un error.")
                
            

    def notificar_otros_usuarios(self, id_cliente_nuevo, respuesta):
        if "usuarios" not in respuesta:
            # Solo me ejecuto si está la key "usuarios" en respuesta
            return

        for socket in self.sockets:
            if socket != id_cliente_nuevo:
                self.enviar_mensaje({
                    "comando": "respuesta_actualizar_usuarios",
                    "usuarios": respuesta["usuarios"]
                }, self.sockets[socket])

    def recibir_mensaje(self, socket_cliente: socket) -> dict:
        """
        Recibe un mensaje del cliente, lo DECODIFICA usando el protocolo
        establecido y lo des-serializa retornando un diccionario.
        """
        # TODO: Completado por estudiante
        largo_archivo = int.from_bytes(socket_cliente.recv(4), byteorder='little')
        datos = bytearray()
        bytes_leidos = 0
        print(f"OK. Ahora sé que debe recibido {largo_archivo} bytes")
        # Ahora leemos el archivo por chunks, de máximo 4096 bytes.
        while len(datos) < largo_archivo:
        # El último recv será probablemente más chico que 4096
            bytes_leer = min(64, largo_archivo - len(datos))
            datos_recibidos = socket_cliente.recv(bytes_leer)
            # Recordemos que el método recv, entrega una cantidad máxima, pero no nos asegura que nos 
            # entregue los 4096 bytes. Es por esto, que la cantidad de bytes que hemos recibido en
            # total, se deben ver siempre en función de lo que retornó el método recv, y no lo que
            # le entregamos como parámetro
            bytes_leidos += len(datos_recibidos)
            print(f"He recibido {len(datos_recibidos)} bytes en el último recv. Van {bytes_leidos} en total.")
            datos.extend(datos_recibidos)
            print(f"¡Listo! He recibido {len(datos)} bytes")
            return self.decodificar_mensaje(datos)

    def enviar_mensaje(self, mensaje: dict, socket_cliente: socket) -> None:
        """
        Recibe una instruccion,
        lo CODIFICA usando el protocolo establecido y lo envía al cliente
        """
        # TODO: Completado por estudiante
        pass

    def enviar_archivo(self, socket_cliente, ruta):
        """
        Recibe una ruta a un archivo a enviar y los separa en chunks de 8 kb
        """
        with open(ruta, "rb") as archivo:
            chunk = archivo.read(8000)
            largo = len(chunk)
            while largo > 0:
                chunk = chunk.ljust(8000, b"\0")  # Padding
                msg = {
                    "comando": "chunk",
                    "argumentos": {"largo": largo, "contenido": chunk.hex()},
                    "ruta": ruta,
                }
                self.enviar_mensaje(msg, socket_cliente)
                chunk = archivo.read(8000)
                largo = len(chunk)

    def eliminar_cliente(self, id_cliente, socket_cliente):
        """
        Elimina un cliente del diccionario de clientes conectados
        """
        try:
            # Cerramos el socket
            self.log(f"Borrando socket del cliente {id_cliente}.")
            socket_cliente.close()
            self.sockets.pop(id_cliente, None)
            self.logica.eliminar_nombre(id_cliente)
            usuarios = ",".join(self.logica.usuarios.values())
            self.notificar_otros_usuarios(id_cliente, {"usuarios": usuarios})

        except KeyError as e:
            self.log(f"ERROR: {e}")

    def codificar_mensaje(self, mensaje):
        try:
            mensaje_json = json.dumps(mensaje)
            mensaje_bytes = mensaje_json.encode()
            return mensaje_bytes
        except json.JSONDecodeError:
            self.log("ERROR: No se pudo codificar el mensaje")
            return b""

    def decodificar_mensaje(self, mensaje_bytes):
        # TODO: Completado por estudiante
        try:
            data = json.loads(mensaje_bytes.recv(4096).decode('utf-8'))
        except ConnectionError:
            print("no se pudo conectar")
        finally:
            return {data}

    def log(self, mensaje: str):
        """
        Imprime un mensaje en consola
        """
        print("|" + mensaje.center(80, " ") + "|")
