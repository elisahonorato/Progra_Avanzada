import os
import os.path

class Path:
    def __init__(self) -> None:
        pass
    def path_main(self):
        if os.path.exists(os.path.join("Tareas","T0")):
            self.path_main = os.path.join("Tareas","T0")
        else:
            self.path_main = os.path
        return str(self.path_main)
        
    def path_partidas(self):
        if os.path.exists(os.path.join("Tareas","T0")):
            self.path_partidas = os.path.join("Tareas","T0", "partidas")
        else:
            self.path_partidas = os.path.join("partidas")
        return str(self.path_partidas)
    
    def path_nombre(self, nombre):
        if os.path.exists(os.path.join("Tareas","T0")):
            self.path_nombre = os.path.join("Tareas","T0", "partidas", f"{nombre}.txt")
        else:
            self.path_nombre = os.path.join("partidas", f"{nombre}.txt")
        return str(self.path_nombre)
    
    def path_añadir(self, nombre):
        if os.path.exists(os.path.join("Tareas","T0")):
            self.path_añadir= os.path.join("Tareas","T0", nombre)
        else:
            self.path_añadir = os.path.join(nombre)
        return str(self.path_añadir)

    