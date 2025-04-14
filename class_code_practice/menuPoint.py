
# 3) En una empresa se almacenaron los sueldos de 10 personas.
# a. Carga de los sueldos en una lista.
# b. Impresión de todos los sueldos.
# c. Cuántos tienen un sueldo superior a $4000.
# d. Retornar el promedio de los sueldos.
# e. Mostrar todos los sueldos que están por debajo del promedio.
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
        print("Empresario",x+1)
        sueldo=int(input("Ingrese el valor de su sueldo: "))
        li.append(sueldo)

    return li 

def mostrarListas(li):
    print("La lista de todos los sueldos es: ",li)

def sueldoM_4000(li):
    cont=0
    for x in li:
        if x > 4000:
            cont=cont+1
    
    print("La cantidad de empresarios que tienen sueldo superior a 4000 es: ",cont)

def promedioS(li):

    for x in li:
        prom=sum(li)/len(li)

    return prom
    
def sueldoD_prom(li,prom):

    listaP=[]

    for x in li:
        if x < prom:
            listaP.append(x)
    
    return listaP



def main():

    #saludo()
    print ("Bienvenidos al programa")
    li=carga_lista()
    prom=promedioS(li)

    Sueldod_prom=sueldoD_prom(li, prom)

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

            mostrarListas(li)
            print ("")
            operacion2()

            input("Has pulsado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu=="3":

            sueldoM_4000(li)

           # operacion()
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu=="4":
            
            print("El promedio de los sueldos es: ",prom)
            
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")
        
        elif opcionMenu=="5":
            
            
            print("Los sueldos que están por debajo del promedio es: ",Sueldod_prom)
            
            input("Has pulsado la opción 5...\npulsa una tecla para continuar")

        elif opcionMenu=="9":
            print("Chao Chao")
            break

        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    print("Hola mundo hasta luego")
main()
