"""
Ventana principal del cliente que se encarga de funcionar como backend de la
mayoria de ventanas, de conectar señales y de procesar los mensajes recibidos
por el cliente
"""
from PyQt5.QtCore import pyqtSignal, QObject

from frontend.ventana_carga import VentanaCarga
from frontend.ventana_login import VentanaLogin
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_final import VentanaFinal
from utils import guardar_archivo


class Interfaz(QObject):
    # Ventana Login
    senal_mostrar_ventana_login = pyqtSignal()
    senal_login_rechazado = pyqtSignal()
    
    # Ventana Carga
    senal_mostrar_ventana_espera = pyqtSignal(str)
    senal_mostrar_ventana_carga = pyqtSignal(str)
    senal_actualizar_oponente = pyqtSignal(str)
    
    # Ventana Principal
    senal_mostrar_ventana_principal = pyqtSignal(list, int)
    senal_mostrar_carta = pyqtSignal(str, str)
    senal_mostrar_carta_ganadora = pyqtSignal(list)
    
    # Ventana Final
    senal_mostrar_ventana_final = pyqtSignal(str)



    def __init__(self):
        super().__init__()
        self.ventana_login = VentanaLogin()
        self.ventana_carga = VentanaCarga()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_final = VentanaFinal()
        # -----------------------------------------
        self.descarga_actual = bytearray()
        self.ronda = 0
        
    def mostrar_ventana_login(self):
        self.ventana_login.mostrar()
    
    def mostrar_ventana_espera(self):
        self.ventana_login.mostrar_espera(str)

    def mostrar_ventana_carga(self, str):
        self.ventana_login.ocultar()
        self.actualizar_jugador(str)
        self.ventana_carga.mostrar()

    def mostrar_ventana_principal(self, baraja, id):
        self.ventana_carga.ocultar()
        self.ventana_principal.mostrar()
        self.ventana_principal.iniciar_ronda(baraja, id)

    def mostrar_ventana_final(self, resultado):
        self.ventana_final.mostrar(resultado)
        self.ventana_principal.salir()

    def actualizar_jugador(self, str):
        self.ventana_carga.label_jugador_1.setText(str)
        self.ventana_principal.label_jugador.setText(str)
        
    def actualizar_oponente(self, str):
        self.ventana_carga.label_jugador_2.setText(str)
        self.ventana_principal.label_oponente.setText(str)
        self.ventana_carga.iniciar_juego()
            

    def manejar_mensaje(self, mensaje: dict):
        """
        Maneja un mensaje recibido desde el servidor.
        """
        try:
            comando = mensaje["comando"]
            respuesta = mensaje["respuesta"]
            user_id = mensaje["user_id"]
            
        except KeyError:
            return {}

        if comando == "respuesta_validacion_login":
            if respuesta["estado"] == "aceptado":
                nombre_usuario = respuesta["nombre_usuario"]
                if respuesta["espera"] == True:
                    self.senal_mostrar_ventana_espera.emit(nombre_usuario)
                elif respuesta["espera"] == False:
                    self.senal_mostrar_ventana_carga.emit(nombre_usuario)
                
            else:
                self.senal_login_rechazado.emit()

        elif comando == "respuesta_validacion_oponente":
            oponente = respuesta["oponente"]
            self.senal_actualizar_oponente.emit(oponente)
            
        elif comando == "respuesta_actualizar_baraja":
            baraja = respuesta["baraja"]
            self.senal_mostrar_ventana_principal.emit(baraja, user_id)
            
        elif comando == "respuesta_mostrar_carta":
            carta = respuesta["carta_mostrar"]
            carta_reemplazante = respuesta['carta_reemplazante']
            self.senal_mostrar_carta.emit(carta, carta_reemplazante)
            
        elif comando == "respuesta_mostrar_ganador":
            cartas_ganadoras = respuesta["cartas_ganadoras"]
            self.senal_mostrar_carta_ganadora.emit(cartas_ganadoras)
            
        elif comando == "respuesta_fin":
            resultado = respuesta["resultado_juego"]
            self.senal_mostrar_ventana_final.emit(resultado)


        elif comando == "chunk":
            parametros = mensaje["argumentos"]
            chunk, largo = parametros["contenido"], parametros.get("largo", 0)
            chunk = bytes.fromhex(chunk)
            chunk = chunk[:largo]  # eliminamos el padding
            self.descarga_actual.extend(chunk)
            if largo < 8000:
                # El ultimo chunk será menor a 8000
                guardar_archivo(self.descarga_actual, mensaje["ruta"])
                self.descarga_actual = bytearray()
