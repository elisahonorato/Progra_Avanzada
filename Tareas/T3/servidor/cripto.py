


def encriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de encriptación
    A = bytearray([msg[i] for i in range(0, len(msg), 3)])
    B = bytearray([msg[i] for i in range(1, len(msg), 3)])
    C = bytearray([msg[i] for i in range(2, len(msg), 3)])
    if len(B) % 2:
        suma_central = B[len(B) // 2 + 1]
    else:
        centro = len(B) // 2
        suma_central = B[centro] + B[centro - 1]
    suma = int(A[0]) + suma_central + C[-1]
    if suma % 2:
        return bytearray(b"\x01") + A + C + B
    else:
        return bytearray(b"\x00") + C + A + B


def desencriptar(msg: bytearray) -> bytearray:
    # Completar con el proceso de desencriptación
    mensaje = msg[1:]
    largo = len(mensaje)
    resto = largo % 3
    largo_a = largo // 3 + int(resto > 0)
    largo_b = largo // 3 + int(resto > 1)
    largo_c = largo // 3
    if msg == bytearray(b''):
        return msg
    if msg[0]:
        A = mensaje[:largo_a]
        C = mensaje[largo_a : largo_a + largo_c]
        B = mensaje[largo_a + largo_c :]
    else:
        C = mensaje[:largo_c]
        A = mensaje[largo_c : largo_a + largo_c]
        B = mensaje[largo_a + largo_c :]
    resultado = bytearray()
    for i in range(largo_c):
        resultado += A[i:i+1]
        resultado += B[i:i+1]
        resultado += C[i:i+1]
    if resto > 0:
        resultado += A[-1:]
    if resto > 1:
        resultado += B[-1:]
    
    return resultado


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b"\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01")
    msg_esperado = bytearray(b"\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01")

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")

    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
