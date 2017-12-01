import quitarRepetidos
import encontrarElemento
preposiciones = ["a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre","hacia", "hasta", "mediante", "para", "por", "según","segun", "sin", "so", "sobre", "tras","versus", "vía","via", "a,", "ante,", "bajo,", "cabe,", "con,", "contra,", "de,", "desde,", "durante,", "en,", "entre,","hacia,", "hasta,", "mediante,", "para,", "por,", "según,","segun,", "sin,", "so,", "sobre,", "tras,","versus,", "vía,","via,"]

def determinarPreposiciones(mensaje):
    if (mensaje==[]):
        return "Vacío"
    else:
        mensaje = mensaje.lower()
        mensaje = mensaje.split()
        return determinarPreposicionesAux(mensaje,[])

def determinarPreposicionesAux(mensaje, resultado):
    if (mensaje==[]):
        return quitarRepetidos.repetidos(resultado)
    elif (encontrarElemento.determinarElemento(mensaje[0],preposiciones)==True):
        return determinarPreposicionesAux(mensaje[1:],resultado+[mensaje[0]])
    else:
        return determinarPreposicionesAux(mensaje[1:],resultado)
