from PyQt5.QtCore import QObject, pyqtSignal
import parametros as p

class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_escena_validacion = pyqtSignal(bool)
    senal_abrir_ventana_principal = pyqtSignal(str)
    senal_abrir_juego = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.instancia_juego = []
        

    def comprobar_usuario(self, usuario: str) -> None:
        valid = False
        errores = ["no Alfanumerico", "Fuera de Rango", "Vacío"]
        if usuario.isalnum():
            errores.remove("no Alfanumerico")
        if p.MIN_CARACTERES <= len(usuario) <= p.MAX_CARACTERES:
            errores.remove("Fuera de Rango")
        if usuario != "":
            errores.remove("Vacío")
        if errores == []:
            valid = True
            self.instancia_juego.append(usuario)
            self.senal_abrir_ventana_principal.emit(str(usuario))
        self.senal_respuesta_validacion.emit(valid, errores)

    def comprobar_escena(self, dict) -> None:
        valid = False
        if True in dict.values() and False in dict.values() and len(dict) == 2:
            valid = True
            for escena, value in dict.items():
                if value:
                    self.instancia_juego.append(escena)
                    self.abrir_juego()
        self.senal_escena_validacion.emit(valid)
    
    def abrir_juego(self):
        self.senal_abrir_juego.emit(self.instancia_juego[0], self.instancia_juego[1])
        
            