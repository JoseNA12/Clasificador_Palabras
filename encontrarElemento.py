def determinarElemento(elemento,diccionario):
    if (elemento == []) or (diccionario== []):
        return False
    elif (elemento == diccionario[0]):
        return True
    else:
        return determinarElemento(elemento,diccionario[1:])
