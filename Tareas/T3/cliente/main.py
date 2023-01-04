"""
Módulo principal del cliente.
"""
import sys
from os.path import join
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from backend.cliente import Cliente
from backend.interfaz import Interfaz
from utils import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    RUTA_ICONO = join(*data_json("RUTA_ICONO"))
    try:
        # =========> Instanciamos la APP <==========
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon(RUTA_ICONO))

        # =========> Iniciamos el cliente <==========
        cliente = Cliente(HOST, PORT)
        interfaz = Interfaz()
        
        # =========> Conectamos señales <==========
        # Cliente
        cliente.senal_manejar_mensaje.connect(
            interfaz.manejar_mensaje
            )
        # Ventana Login
        interfaz.ventana_login.senal_enviar_login.connect(
            cliente.enviar
        )
        cliente.senal_mostrar_ventana_login.connect(
            interfaz.mostrar_ventana_login
            )
        interfaz.senal_login_rechazado.connect(
            interfaz.ventana_login.mostrar_error
            )
        # Ventana Carga
        interfaz.senal_mostrar_ventana_espera.connect(
             interfaz.mostrar_ventana_espera
        )
        interfaz.senal_mostrar_ventana_carga.connect(
             interfaz.mostrar_ventana_carga
        )
        interfaz.ventana_carga.senal_volver.connect(
             interfaz.ventana_login.mostrar
        )
        interfaz.senal_actualizar_oponente.connect(
             interfaz.actualizar_oponente
             )
        interfaz.ventana_carga.senal_enviar_inicio.connect(
             cliente.enviar
        )
        # Ventana Principal
        interfaz.senal_mostrar_ventana_principal.connect(
            interfaz.mostrar_ventana_principal
        )

        interfaz.ventana_principal.senal_enviar_ronda.connect(
            cliente.enviar
        )
        interfaz.senal_mostrar_carta.connect(
            interfaz.ventana_principal.mostrar_carta
        )
        interfaz.senal_mostrar_carta_ganadora.connect(
            interfaz.ventana_principal.mostrar_carta_ganadora
        )
        interfaz.senal_mostrar_ventana_final.connect(
            interfaz.mostrar_ventana_final
        )
        interfaz.ventana_final.senal_volver.connect(
             interfaz.ventana_login.mostrar
        )

        
        sys.exit(app.exec_())

    except ConnectionError as e:
        print("Ocurrió un error.", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        cliente.salir()
        sys.exit()