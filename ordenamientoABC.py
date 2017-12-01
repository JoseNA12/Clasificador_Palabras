def ordenamiento(mensaje):
    mensaje = mensaje.lower()
    mensaje = mensaje.split()
    numero = len(mensaje)
    indice= 0
    while (indice < numero):
        indiceDos = indice
        while (indiceDos < numero):
            if(mensaje[indice] > mensaje[indiceDos]):
                resultado = mensaje[indice]
                mensaje[indice] = mensaje[indiceDos]
                mensaje[indiceDos] = resultado
            indiceDos += 1
        indice += 1
 
    return (" ".join(mensaje)) #Evita inconvenientes en el momento de tokenizar

