import quitarRepetidos

def determinarVerbos(mensaje):
    if (mensaje == []):
        return "Vacío"
    else:
        mensaje = mensaje.lower() #Para evitar inconvenientes con las mayusculas 
        mensaje=mensaje.split()
        return determinarVerbosAux(mensaje,[])

def determinarVerbosAux(mensaje,resultado):
    if (mensaje == []):
        return quitarRepetidos.repetidos(resultado)
    else:
        indice = len(mensaje[0])
    #Infinitivos
        if (mensaje[0][indice-1]=="r") and (mensaje[0][indice-2]=="a"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="r") and (mensaje[0][indice-2]=="e"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="r") and (mensaje[0][indice-2]=="i"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif ((mensaje[0][indice-1]==",")) and (mensaje[0][indice-2]=="r") and (mensaje[0][indice-3]=="a"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif ((mensaje[0][indice-1]==",")) and (mensaje[0][indice-2]=="r") and (mensaje[0][indice-3]=="e"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif ((mensaje[0][indice-1]==",")) and (mensaje[0][indice-2]=="r") and (mensaje[0][indice-3]=="i"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
    #Gerundios
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="d") and (mensaje[0][indice-3]=="n") and (mensaje[0][indice-4]=="a"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="d") and (mensaje[0][indice-3]=="n") and (mensaje[0][indice-4]=="e") and (mensaje[0][indice-5]=="i"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o") and (mensaje[0][indice-3]=="d") and (mensaje[0][indice-4]=="n") and (mensaje[0][indice-5]=="a"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o") and (mensaje[0][indice-3]=="d") and (mensaje[0][indice-4]=="n") and (mensaje[0][indice-5]=="e") and (mensaje[0][indice-6]=="i"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
    #Participios
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="d") and (mensaje[0][indice-3]=="a"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="d") and (mensaje[0][indice-3]=="i"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="t"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="s"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]=="o") and (mensaje[0][indice-2]=="h") and (mensaje[0][indice-3]=="c"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o") and (mensaje[0][indice-3]=="d") and (mensaje[0][indice-4]=="a"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o") and (mensaje[0][indice-3]=="d") and (mensaje[0][indice-4]=="i"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o")  and (mensaje[0][indice-3]=="t"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o")  and (mensaje[0][indice-3]=="s"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        elif (mensaje[0][indice-1]==",") and (mensaje[0][indice-2]=="o") and (mensaje[0][indice-3]=="h")  and (mensaje[0][indice-4]=="c"):
            return determinarVerbosAux(mensaje[1:],resultado+[mensaje[0]])
        
        else:
            return determinarVerbosAux(mensaje[1:],resultado)
