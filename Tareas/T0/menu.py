from string import ascii_lowercase as letras

# Diccionario por comprensión
numero_por_letra = {letras[i].lower(): i + 1 for i in range(len(letras))}
inp = "a"
letra = inp.lower()
numero = numero_por_letra[letra]
if letra in numero_por_letra:
    print(numero)