import quitarRepetidos
import encontrarElemento

articulos = ["el","el,","el.","la","los","las","un","una","unos","unos","unas","lo","al","del","el,","la,","los,","las,","un,","una,","unos,","unos,","unas,","lo,","al,","del,"]

def determinarArticulos(mensaje):
    if (mensaje==[]):
        return "Vacío"
    else:
        mensaje = mensaje.lower()
        mensaje=mensaje.split()
        return determinarArticulosAux(mensaje,[])

def determinarArticulosAux(mensaje, resultado):
    if (mensaje==[]):
        return (quitarRepetidos.repetidos(resultado))
    elif (encontrarElemento.determinarElemento(mensaje[0],articulos)==True):
        return determinarArticulosAux(mensaje[1:],resultado+[mensaje[0]])
    else:
        return determinarArticulosAux(mensaje[1:],resultado)

