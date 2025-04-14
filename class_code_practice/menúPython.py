# 1) Escriba un programa en Phyton Modular que permita:
#       a. Crear una lista de palabras. Para ello, el programa tiene que
#       pedir un número y luego solicitar ese número de palabras para
#       crear la lista.

#       b. Mostrar la lista

#       c. Pedir una palabra y decir cuántas veces aparece esa palabra en
#       la lista.

#       d. Pedir dos palabras y sustituir la primera por la segunda en la
#       lista.

#       e. Pedir una palabra y eliminar esa palabra de la lista.

#       f. Crear una nueva lista de palabras y, eliminar de la primera lista
#       los nombres de la segunda lista.

#       g. Crear una segunda lista igual a la primera, pero al revés (no se
#       trata de escribir la lista al revés, sino de crear una lista distinta).

#       h. Eliminar los elementos repetidos (dejando únicamente el
#       primero de los elementos repetidos).

#       i. Crear una nueva lista de palabras y escribir las siguientes listas
#       (en las que no debe haber repeticiones):
#           • Lista de palabras que aparecen en las dos listas.

#           • Lista de palabras que aparecen en la primera lista, pero
#           no en la segunda.

#           • Lista de palabras que aparecen en la segunda lista, pero
#           no en la primera.

#           • Lista de palabras que aparecen en ambas listas.

"""
ASIGNATURA:ALGORITMOS Y PROGRAMACION
# OBJETIVO: Utilización de un menú
# AUTOR: Andersson David Sánchez Méndez
# FECHA:05/11/23
"""

import os

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
        if os.name == "posix":
           os.system ("clear")  
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
           os.system ("cls")
   
def menu():
	
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t4 - cuarta opción")
	print ("\t9 - salir")
        


def operacion1():
    print("Hola 1")
    

def operacion2():
    print("Hola")

def carga_lista():
    li=[] #Se crea la lista vacía para después llenarla
    n=int(input("Digite la cantidad de número de palabras: "))
    for x in range (0,n):
        #númeroL_pal=int(input("Digite el número de letras por palabra: "))
    
        #for x in range (0,n):
        palabra=input("Ingrese palabra: ")
        li.append(palabra)
    
        #print (li)
    return li
          
def mostrar_lista(lista):

    for elem in lista:
        print(elem, end = " ") 

def pedirPalabraRepetida(lista):
    palabra = input("Ingrese palabra a buscar: ")
    cantidad = lista.count(palabra)
    print(palabra,"aparece",cantidad,"veces en la lista. " )

def pedir2PalabrasSustituir(lista):
    palabra1 = input("Ingrese palabra a reemplazar: ")
    palabra2 = input("Ingrese palabra de reemplazo: ")
    if palabra1 in lista:
        index = lista.index(palabra1)
        lista[index] = palabra2
        print("Palabra reemplazada con éxito.")
    else:
        print(palabra1,"no se encontró en la lista.")

def palabraEliminar(lista):
    palabra = input("Ingrese palabra a eliminar: ")
    if palabra in lista:
        lista.remove(palabra)
        print(palabra,"ha sido eliminada de la lista." )
    else:
        print(palabra,"no se encontró en la lista.")

def operacion_f(lista_principal):
    lista_a_eliminar = carga_lista()
    lista_principal = [word for word in lista_principal if word not in lista_a_eliminar]
    print("Elementos eliminados de la lista principal.")
    return lista_principal

# Operación g: Crear una segunda lista igual a la primera, pero al revés.
def operacion_g(lista_principal):
    lista_reversa = lista_principal[::-1]
    print("Nueva lista creada al revés.")
    return lista_reversa

# Operación h: Eliminar los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
def operacion_h(lista_principal):
    lista_sin_repetir = []
    for word in lista_principal:
        if word not in lista_sin_repetir:
            lista_sin_repetir.append(word)
    print("Elementos repetidos eliminados.")
    return lista_sin_repetir

# Operación i: Crear nuevas listas sin repeticiones.
def operacion_i(lista_principal):
    nueva_lista = carga_lista()
    interseccion = list(set(lista_principal) & set(nueva_lista))
    solo_en_lista1 = list(set(lista_principal) - set(nueva_lista))
    solo_en_lista2 = list(set(nueva_lista) - set(lista_principal))
    palabras_repetidas = list(set(lista_principal) & set(nueva_lista))
    return interseccion, solo_en_lista1, solo_en_lista2, palabras_repetidas

def main():

    #saludo()
    print ("Bienvenidos al programa")

    lista=carga_lista()

    while True:
        borrarPantalla()
        menu()
        
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu=="1":
            carga_lista()
            print ("")

            operacion1()

            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            
           
        elif opcionMenu=="2":
            mostrar_lista(lista)
            print ("")

            operacion2()

            input("Has pulsado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu=="3":
            pedirPalabraRepetida(lista)
            print ("")
           # operacion()
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu=="4":
            pedir2PalabrasSustituir(lista)
            print ("")
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")

        elif opcionMenu=="5":
            palabraEliminar(lista)
            print ("")
            input("Has pulsado la opción 5...\npulsa una tecla para continuar")

        elif opcionMenu=="6":
            operacion_f(lista)
            print ("")
            input("Has pulsado la opción 6...\npulsa una tecla para continuar")

        elif opcionMenu=="7":
            operacion_g(lista)
            print ("")
            input("Has pulsado la opción 7...\npulsa una tecla para continuar")
        
        elif opcionMenu=="8":
            operacion_h(lista)
            print ("")
            input("Has pulsado la opción 8...\npulsa una tecla para continuar")

        elif opcionMenu=="9":
            operacion_i(lista)
            print ("")
            input("Has pulsado la opción 9...\npulsa una tecla para continuar")

        elif opcionMenu=="10":
            print("Chao Chao")
            break

        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    print("Hola mundo hasta luego")

main()


