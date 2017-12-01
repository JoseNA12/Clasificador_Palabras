import quitarRepetidos
import encontrarElemento
numeros= ["0","1","2","3","4","5","6","7","8","9","-"]
def determinarNumeros(mensaje):
    if (mensaje==[]):
        return "Vacío"
    else:
        mensaje = mensaje.lower()
        mensaje = mensaje.split()
      
        
        return determinarNumerosAux(mensaje)
    
def determinarNumerosAux(mensaje):
    indiceConjunto= 0
    resultado = []
    
    while indiceConjunto < len(mensaje):
        indiceElemento=0
        numero= ""
        
        while indiceElemento < len(mensaje[indiceConjunto]):
            
        
            if ((encontrarElemento.determinarElemento(mensaje[indiceConjunto][indiceElemento],numeros)) == True):
                numero += mensaje[indiceConjunto][indiceElemento]
             
            indiceElemento+= 1
            
        if numero == mensaje[indiceConjunto]:
            resultado += [numero]
            
            
        indiceConjunto+= 1
    resultado= quitarRepetidos.repetidos(resultado)
    
    return ordenamientoNumeral(resultado)
   

def ordenamientoNumeral(mensaje):
    
    numero = len(mensaje)
    indice= 0
    while (indice < numero):
        indiceDos = indice
        while (indiceDos < numero):
            if int(mensaje[indice]) > int(mensaje[indiceDos]):
                resultado = mensaje[indice]
                mensaje[indice] = mensaje[indiceDos]
                mensaje[indiceDos] = resultado
            indiceDos += 1
        indice += 1
    return mensaje
    
