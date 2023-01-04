from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, set)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, usuario: str, contrasena: str) -> None:
        valid = False
        errores = set()
        if not usuario.isalnum():
            errores.add("usuario")
        if contrasena in p.CONTRASENAS_PROHIBIDAS:
            errores.add("contraseña")
        if errores == set():
            valid = True
            self.senal_abrir_juego.emit((usuario))
        self.senal_respuesta_validacion.emit(valid, errores)
