import preposiciones
import articulos
import verbos
import numeros
import pronombres
import quitarRepetidos
import encontrarElemento


def sinClasificar(mensaje):
    if (mensaje==[]):
        return "Vacío"
    else:
        preposicion= preposiciones.determinarPreposiciones(mensaje)
        articulo= articulos.determinarArticulos(mensaje)
        verbo= verbos.determinarVerbos(mensaje)
        numero= numeros.determinarNumeros(mensaje)
        pronombre= pronombres.determinarPronombres(mensaje)
        mensaje = mensaje.lower()
        mensaje = mensaje.split()
        
        return sinClasificarAux(mensaje, preposicion,articulo,verbo,numero,pronombre,[])
    
def sinClasificarAux(mensaje,preposicion,articulo,verbo,numero,pronombre,resultado):
    if mensaje==[]:
        return (quitarRepetidos.repetidos(resultado))
    else:
        if (encontrarElemento.determinarElemento(mensaje[0],preposicion)==False) and (encontrarElemento.determinarElemento(mensaje[0],articulo)==False) and (encontrarElemento.determinarElemento(mensaje[0],verbo)==False) and (encontrarElemento.determinarElemento(mensaje[0],numero)==False) and (encontrarElemento.determinarElemento(mensaje[0],pronombre)==False):
            return sinClasificarAux(mensaje[1:],preposicion,articulo,verbo,numero,pronombre,resultado + [mensaje[0]])
        
        else:
            return sinClasificarAux(mensaje[1:],preposicion,articulo,verbo,numero,pronombre,resultado )

