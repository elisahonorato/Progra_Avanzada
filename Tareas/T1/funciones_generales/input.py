def get_input(lista):
    inp = input()
    if inp not in {str(i + 1) for i in range(lista)} or inp == str(0):
        print(f"Debes ingresar un número dentro del rango")
        return get_input(lista)
    elif str(inp) == str(lista - 1):
        return "Volver"
    elif str(inp) == str(lista):
        return "Salir"
    return int(inp)