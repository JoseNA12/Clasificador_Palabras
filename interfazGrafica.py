from tkinter import *
from tkinter.ttk import * # Al importar (.ttk)-> Cambia el aspecto de la ventana(Botones, labels, textos..)(Estética)
from tkinter import filedialog # Hace posible el abrir y manipular archivos
from tkinter import messagebox # Hace posible imprimir mensajes de advertencia
import time #Obtiene todos los datos en lo que respecta: hora, mes, año, etc
import articulos
import preposiciones
import pronombres
import verbos
import numeros
import sinClasificar
import ordenamientoABC

#Funciones que se necesitan en la ventana principal

def tokenizar():
    borrarTokens()
    
    texto = textoDocumento.get('1.0','end-1c') #Permite obtener lo que se escribe en textoDocumento y así, poder tokenizar
    texto = ordenamientoABC.ordenamiento(texto) #Ordena alfabeticamente cada palabra
    
    articuloLista = arbol.insert("Documento", "end","Artículos",text="Artículos") 
    preposicionLista = arbol.insert("Documento", "end","Preposiciones",text="Preposiciones")
    pronombreLista = arbol.insert("Documento", "end","Pronombres",text="Pronombres")
    verboLista = arbol.insert("Documento", "end","Verbos",text="Verbos")
    numeroLista = arbol.insert("Documento", "end","Números",text="Números")
    sinClasificarLista = arbol.insert("Documento", "end","Sin clasificar",text="Sin clasificar")
    
    for articulo in articulos.determinarArticulos(texto):
        (arbol.insert(articuloLista,"end",text=articulo))

    for preposicion in preposiciones.determinarPreposiciones(texto):
        (arbol.insert(preposicionLista,"end",text=preposicion))

    for pronombre in pronombres.determinarPronombres(texto):
        (arbol.insert(pronombreLista,"end",text=pronombre))

    for verbo in verbos.determinarVerbos(texto):
        (arbol.insert(verboLista,"end",text=verbo))

    for numero in numeros.determinarNumeros(texto):
        (arbol.insert(numeroLista,"end",text=numero))

    for noClasificado in sinClasificar.sinClasificar(texto):
        (arbol.insert(sinClasificarLista,"end",text=noClasificado))

def eliminarTexto(): #Función que elimina que lo se escribe en el apartado "Documento"
    textoDocumento.delete('1.0', END) # '1.0' -> Toma el texto desde el principio | 'END' -> Elimina el texto hasta el final

def borrarTokens():
    for directory in arbol.get_children():
        for child in arbol.get_children(directory):
            arbol.delete(child) #Obtiene cada subelemento del treeView, para luego ser borrados

def abrirArchivo(): #Abrir y leer el archivo
    tipoArchivo = [("Archivos de texto",".txt")]
    ventanaAbrir = filedialog.Open(filetypes = tipoArchivo) #Muestra la ventana para abrir el .txt
    mostrarTexto = ventanaAbrir.show() #Muestra el texto una vez selecionado en el 'Text', en este caso en textoDocumento

    if (mostrarTexto != ''):
        texto = leerArchivo(mostrarTexto)
        textoDocumento.insert(END, texto) #Se inserta el archivo seleccionado(.txt) en la caja de texto ->(textoDocumento)

def leerArchivo(archivo):
    try:
        abrirTexto = open(archivo, "r")
        texto = abrirTexto.read()
        return texto #Retorna el texto para finalmente ser mostrado en la caja del textoDocumento

    except IOError:
        return -1


def crearHmtl():
    texto = textoDocumento.get('1.0','end-1c')
    textOrdenado = ordenamientoABC.ordenamiento(texto)

    elementos = [articulos.determinarArticulos(textOrdenado)]+[preposiciones.determinarPreposiciones(textOrdenado)]+[pronombres.determinarPronombres(textOrdenado)]+[verbos.determinarVerbos(textOrdenado)]+[numeros.determinarNumeros(textOrdenado)]+[sinClasificar.sinClasificar(textOrdenado)]

    try:
        htmlArchivo = open("Analisis-"+time.strftime('%d-%b-%y-')+time.strftime('%I-%M-%S')+".html", "a") #.strtime -> parámetros del modulo 'time'
        htmlArchivo.write("<!DOCTYPE html>")
        htmlArchivo.write("<head>")
        htmlArchivo.write("<title>Tarea programada 2</title>")
        htmlArchivo.write("</head>")
        htmlArchivo.write("<body>")
        htmlArchivo.write("    <header>")
        htmlArchivo.write("       <h1>Texto ingresado:</h1>")
        htmlArchivo.write("       <p>"+texto+"</p>")
        htmlArchivo.write("    </header>")
        htmlArchivo.write("    <section>")
        htmlArchivo.write("       <article>")
        htmlArchivo.write("             <table border='5' style='width:90%' id='mytable' class='tabla'>")
        htmlArchivo.write("                <thead>")
        htmlArchivo.write("                     <tr>")
        htmlArchivo.write("                       <th scope='colgroup' colspan='6'>Analisis del documento</th>")
        htmlArchivo.write("                   </tr")
        htmlArchivo.write("                 <tr>")
        htmlArchivo.write("                   <th><span>Artículos</span></th>")
        htmlArchivo.write("                   <th><span>Preposiciones</span></th>")
        htmlArchivo.write("                   <th>Pronombres</span></th>")
        htmlArchivo.write("                   <th><span> Verbos </span></th> ")
        htmlArchivo.write("                   <th><span>Numeros</span></th>")
        htmlArchivo.write("                   <th><span>Sin Clasificar</span></th>")
        htmlArchivo.write("                </tr>")
        htmlArchivo.write("                </thead>")
        htmlArchivo.write("                  <tbody>")
        #En caso de que la lista este vacía para que no se genere un IndexError
        elementos[0]+=" "
        elementos[1]+=" "
        elementos[2]+=" "
        elementos[3]+=" "
        elementos[4]+=" "
        elementos[5]+=" "

        fila = 0
        while fila < len(elementos[0]) and fila < len(elementos[1]) and fila < len(elementos[2]) and fila < len(elementos[3]) and fila < len(elementos[4]) and fila < len(elementos[5]):
            
            if len(elementos[0]) < len(elementos[1]) or len(elementos[0]) < len(elementos[2]) or len(elementos[0]) < len(elementos[3]) or len(elementos[0]) < len(elementos[4]) or len(elementos[0]) < len(elementos[5]):
                elementos[0]+=" "

            if len(elementos[1]) < len(elementos[0]) or len(elementos[1]) < len(elementos[2]) or len(elementos[1]) < len(elementos[3]) or len(elementos[1]) < len(elementos[4]) or len(elementos[1]) < len(elementos[5]):
                elementos[1]+=" "

            if len(elementos[2]) < len(elementos[0]) or len(elementos[2]) < len(elementos[1]) or len(elementos[2]) < len(elementos[3]) or len(elementos[2]) < len(elementos[4]) or len(elementos[2]) < len(elementos[5]):
                elementos[2]+=" "

            if len(elementos[3]) < len(elementos[0]) or len(elementos[3]) < len(elementos[1]) or len(elementos[3]) < len(elementos[2]) or len(elementos[3]) < len(elementos[4]) or len(elementos[3]) < len(elementos[5]):
                elementos[3]+=" "

            if len(elementos[4]) < len(elementos[0]) or len(elementos[4]) < len(elementos[1]) or len(elementos[4]) < len(elementos[2]) or len(elementos[4]) < len(elementos[3]) or len(elementos[4]) < len(elementos[5]):
                elementos[4]+=" "
                    
            if len(elementos[5]) < len(elementos[0]) or len(elementos[5]) < len(elementos[1]) or len(elementos[5]) < len(elementos[2]) or len(elementos[5]) < len(elementos[3]) or len(elementos[5]) < len(elementos[4]):
                elementos[5]+=" "

            if elementos[0][fila]!=[] or elementos[1][fila]!=[] or elementos[2][fila]!=[] or elementos[3][fila]!=[] or elementos[4][fila]!=[] or elementos[5][fila]!=[]:
                htmlArchivo.write("                <tr>")
                htmlArchivo.write("                  <td>"+elementos[0][fila]+"</td>")
                htmlArchivo.write("                  <td>"+elementos[1][fila]+"</td>")
                htmlArchivo.write("                  <td>"+elementos[2][fila]+"</td>")
                htmlArchivo.write("                  <td>"+elementos[3][fila]+"</td>")
                htmlArchivo.write("                  <td>"+elementos[4][fila]+"</td>")
                htmlArchivo.write("                  <td>"+elementos[5][fila]+"</td>")
                htmlArchivo.write("                </tr>")
                fila += 1

            else:

                htmlArchivo.write("                  <td>""</td>")

        htmlArchivo.write("                <tbody>")
        htmlArchivo.write("         </table>")
        htmlArchivo.write("       </article>")
        htmlArchivo.write("    </section>")
        htmlArchivo.write("</body>")
        htmlArchivo.write("</html>")
    
        htmlArchivo.close()

        return True #Quiere decir que el archivo ha sido creado correctamente
    except IOError:
        return -1
        

#Caracteristicas de la ventana principal (Etiquetas, labels, botones..)

proyecto = Tk() #Hace posible la ejecución de la ventana

proyecto.title("Tarea Programada 2")
proyecto.geometry("990x540")
proyecto.minsize(width=990,height=540)
proyecto.maxsize(width=990,height=540)

#Sección: Documento

etiqueta1 = Label(proyecto, text="Documento:")
etiqueta1.place(x=28,y=25)

scrollbar = Scrollbar(proyecto)
scrollbar.place(x=435,y=45,height=435)

textoDocumento = Text(proyecto,width=50,height=27, wrap=WORD, yscrollcommand=scrollbar.set) #wrap=WORD -> Agarra el texto del textoDocumento para que el scrollbar works
textoDocumento.place(x=30,y=45)
scrollbar.config(command=textoDocumento.yview)#Se 'asigna' al textoDocumento para que funcion con él.

botonLimpiar = Button(proyecto, text="    Limpiar    ", command = lambda: eliminarTexto()==borrarTokens()) # lambda:->Sirve para que la accion que hace el boton solo la realize cuando se preciona dicho boton
botonLimpiar.place(x=227,y=495)

botonAbrirArchivo = Button(proyecto, text="    Abrir archivo..    ", command = lambda: abrirArchivo())
botonAbrirArchivo.place(x=325,y=495)

#Sección: Estructura de listas

etiqueta2 = Label(proyecto, text="Estructura de datos:")
etiqueta2.place(x=518,y=25)

botonTokenizar = Button(proyecto, text="    Tokenizar    ", command = lambda: tokenizar())
botonTokenizar.place(x=670, y=495)

    #arbol -> Estructura de la tokenizacion

arbol = Treeview(proyecto)
arbol.place(x=520,y=45,height=435)
#documento -> Estructura 'padre' del treeview 
documento = arbol.insert("", 1,"Documento",text="Documento")

#Sección: HTML

etiqueta3 = Label(proyecto, text="Generar html:")
etiqueta3.place(x=810,y=25)

botonGenerar = Button(proyecto, text="    Crear archivo HTML   ",command = lambda: crearHmtl()== messagebox.showinfo('Atención!','El archivo se ha generado correctamente'))
botonGenerar.place(x=810,y=52)

proyecto.mainloop()


