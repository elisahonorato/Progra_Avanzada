def get_input(op):
    inp = input()
    if inp not in {str(i) for i in range(op + 1)}:
        print(f"Debes ingresar un número dentro del rango")
        return get_input(op)
    return int(inp)

def get_input_abc(maximo_largo):
    inp = input()
    letra = inp[0].lower()
    codigo = ord(letra) - 97
    if codigo < 0 or codigo > maximo_largo:
        print('Ingrese una letra del abecedario correcta')
        return get_input_abc(maximo_largo)
    return codigo




    
