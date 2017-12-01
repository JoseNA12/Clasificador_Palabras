
def repetidos(lista):
    resultado=[]
    indice= 0

    while indice < len(lista):
        if lista[indice] not in resultado:
            resultado.append(lista[indice])
        indice+=1
    return resultado
