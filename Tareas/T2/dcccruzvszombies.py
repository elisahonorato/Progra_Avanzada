from PyQt5.QtWidgets import QApplication

from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_ronda import VentanaPostRonda
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, Usuario
from backend.elementos_juego import Planta, PlantaClasica
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_ranking import VentanaRanking


class DCCruz(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        # Instanciar Ventanas
        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_juego = VentanaJuego()
        self.ventana_ranking = VentanaRanking()
        self.ventana_post_ronda = VentanaPostRonda()

        # Instanciar Lógicas
        self.usuario = Usuario()
        self.logica_inicio = LogicaInicio()
        self.logica_juego = LogicaJuego()

        # Conectar Señales
        self.conectar_inicio()
        self.conectar_juego()
        self.conectar_ranking()
        self.conectar_post_ronda()

    def conectar_inicio(self):
        self.ventana_inicio.senal_enviar_login.connect(
            self.logica_inicio.comprobar_usuario
        )
        self.logica_inicio.senal_respuesta_validacion.connect(
            self.ventana_inicio.recibir_validacion
        )
        self.logica_inicio.senal_abrir_ventana_principal.connect(
            self.ventana_principal.mostrar_ventana
        )
        self.ventana_principal.senal_enviar_escena.connect(
            self.logica_inicio.comprobar_escena
        )
        self.logica_inicio.senal_escena_validacion.connect(
            self.ventana_principal.recibir_validacion
        )
        self.logica_inicio.senal_abrir_juego.connect(
            self.ventana_juego.mostrar_ventana
        )
        self.ventana_juego.senal_volver_inicio.connect(
            self.ventana_inicio.show
        )

    def conectar_juego(self):
        self.ventana_juego.senal_iniciar_juego.connect(
            self.logica_juego.iniciar_juego
        )
        self.ventana_juego.senal_iniciar_ronda.connect(
            self.logica_juego.iniciar_ronda
        )
        self.logica_juego.senal_actualizar.connect(
            self.ventana_juego.actualizar_datos
        )
        self.ventana_juego.senal_tecla.connect(
            self.logica_juego.recibir_teclas
        )
        self.ventana_juego.senal_mouse_izquierdo.connect(
            self.logica_juego.tienda_plantas
        )
        self.logica_juego.senal_update_position.connect(
            self.ventana_juego.actualizar_elementos
        )
        self.ventana_juego.senal_mouse_derecho.connect(
            self.logica_juego.recolectar_soles
        )
        self.logica_juego.senal_cerrar_ventana_juego.connect(
            self.ventana_juego.salir
    )
        self.logica_juego.senal_termino_juego.connect(
            self.ventana_post_ronda.abrir
        )
    def conectar_ranking(self):
        self.ventana_inicio.senal_ver_ranking.connect(
            self.ventana_ranking.show
        )
        self.ventana_ranking.senal_volver_inicio.connect(
            self.ventana_inicio.show
        )

    def conectar_post_ronda(self):
        self.ventana_post_ronda.senal_abrir_inicio.connect(
            self.ventana_inicio.show)
            
        self.ventana_post_ronda.senal_cerrar_juego.connect(self.exit)

        self.ventana_post_ronda.senal_siguiente_ronda.connect(
            self.ventana_juego.mostrar_ventana
            )
        self.ventana_post_ronda.senal_siguiente_ronda.connect(
            self.logica_juego.iniciar_ronda
            )
        self.ventana_juego.senal_volver_inicio.connect(
            self.ventana_inicio.show
        )

    def iniciar(self):
        self.ventana_inicio.show()
