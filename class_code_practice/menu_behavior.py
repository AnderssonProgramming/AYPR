# 2) Hacer un programa en Phyton Modular que permita:
# a. Cargar una lista de 10 elementos enteros
# b. Generar dos listas a partir de la primera. En una guardar los
# valores positivos y en otra los negativos.
# c. Imprimir las dos listas generadas
"""
ASIGNATURA:ALGORITMOS Y PROGRAMACION
# OBJETIVO: Utilización de un menú
# AUTOR:Andersson David Sánchez Méndez
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
	print ("\t4 - tercera opción")
	print ("\t9 - salir")
        


def operacion1():
    print("Hola 1")
    

def operacion2():
    print("Hola")

def carga_lista():
    li=[] #Se crea la lista vacía para después llenarla

    for x in range (0,10):

        numeroE=int(input("Ingrese un número entero diferente de 0: "))
        li.append(numeroE)
    
        #print (li)
    return li 

def listaNumerosP(li):
    listaP=[]
    for x in li:
        if x >0:
            listaP.append(x)
    
    return listaP

def listaNumerosN(li):
    listaN=[]
    for x in li:
        if x<0:
            listaN.append(x)
    
    return listaN

def mostrarListas(listaP, listaN):

    print("La lista con números enteros positivos es: ",listaP)
    print("La lista con números enteros negativos es: ",listaN)


def main():

    #saludo()
    print ("Bienvenidos al programa")
    li=carga_lista()
    listaPositivos=listaNumerosP(li)
    listaNegativos=listaNumerosN(li)
    
    while True:
        borrarPantalla()
        menu()
        
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu=="1":

            print ("")
            carga_lista()
            operacion1()

            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            
           
        elif opcionMenu=="2":

            listaNumerosP(li)


            print ("")

            operacion2()

          
            
            
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu=="3":

            listaNumerosN(li)
            print ("")
           # operacion()
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu=="4":
            mostrarListas(listaPositivos, listaNegativos)
            print ("")
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")

        elif opcionMenu=="9":
            print("Chao Chao")
            break

        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    print("Hola mundo hasta luego")
main()
