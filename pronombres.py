import quitarRepetidos
import encontrarElemento
pronombres= ["yo","me","mí","mi","conmigo","nosotros","nosotras","nos","tú","tu","te","ti","contigo","vosotros","vosotras","vos","él","ella","se","consigo","le","les","mio","mío","mio,","mí,","consigo,","mia","mía","mios","míos","mias","mías","nuestro","nuestra","nuestros","nuestras","tuyo","tuya","tuyos","vuestro","vuestra","vuestros","vuestras","suyo","suya","suyos","suyas"]

def determinarPronombres(mensaje):
    if (mensaje==[]):
        return "Vacío"
    else:
        mensaje = mensaje.lower()
        mensaje = mensaje.split()
       
        return determinarPronombresAux(mensaje,[])

def determinarPronombresAux(mensaje, resultado):
    if (mensaje==[]):
        return quitarRepetidos.repetidos(resultado)
    elif (encontrarElemento.determinarElemento(mensaje[0],pronombres)==True):
        return determinarPronombresAux(mensaje[1:],resultado+[mensaje[0]])
    else:
        return determinarPronombresAux(mensaje[1:],resultado)
