import sys


from dcccruzvszombies import DCCruz

if __name__ == '__main__':
    def hook(type_, value, traceback):
        print(traceback)
    sys.__excepthook__ = hook

    juego = DCCruz(sys.argv)
    juego.iniciar()
    sys.exit(juego.exec())
    # actualizar orden de archivos
