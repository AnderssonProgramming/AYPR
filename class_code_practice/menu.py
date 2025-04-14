"""
ASIGNATURA:ALGORITMOS Y PROGRAMACION
# OBJETIVO: Utilización de un menú
# AUTOR: Andersson David Sánchez Méndez
# FECHA:08/11/23
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
    lista_alumnos=[] #Se crea la lista vacía para después llenarla
    n=int(input("Digite la cantidad de número de alumnos: "))
    for x in range (0,n):
        
        lista2=[]
        estudiante=input("Digite su nombre: ")
        lista2.append(estudiante)
        print(estudiante)
        nota1=int(input("Dame la nota 1: "))
        lista2.append(nota1)
        nota2=int(input("Dame la nota 2: "))
        lista2.append(nota2)
        nota3=int(input("Dame la nota 3: "))
        lista2.append(nota3)

        lista_alumnos.append(lista2)
        
    
    print (lista_alumnos)

    return lista_alumnos
          
def mostrar_lista(listaalumnos):

    for elem in listaalumnos:
        for pos in elem:
            print("[",pos,"]",end=" ")

def mostrarAlumnosNotas(listaalumnos):

    for i in range(len(listaalumnos)):
        
        print(listaalumnos[i][0],listaalumnos[i][1],listaalumnos[i][2],listaalumnos[i][3]) 


def DefinitivaAlumno(listaalumnos):
    listaDefinitiva=[]
    for i in range (len(listaalumnos)):

        definitiva=listaalumnos[i][1]*0.3+listaalumnos[i][2]*0.3+listaalumnos[i][3]*0.4

        print("Su definitiva es: ",definitiva)

        listaDefinitiva.append(definitiva)
    
    return listaDefinitiva


def promedioClase(listadefinitiva):

    sumaDefinitiva=0

    for i in range (len(listadefinitiva)):
        sumaDefinitiva=sumaDefinitiva+listadefinitiva[i]
    
    sumaPromedio=sumaDefinitiva/len(listadefinitiva)

    print("El promedio de la clase es: ",sumaPromedio)
        
        
def alumnoMayorNota(listadefinitiva,listaalumnos):
    MayorNota=[0]
    for i in listadefinitiva:
        if i > MayorNota:
            MayorNota=i
    
    alumnoMayorNota=listadefinitiva.index(MayorNota)

    print("El alumno con mayor nota es: ",listaalumnos[alumnoMayorNota][0],"con una nota de",MayorNota)


def main():

    #saludo()
    print ("Bienvenidos al programa")

    lista=carga_lista()
    listaDefinitiva=DefinitivaAlumno(lista)
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
            mostrarAlumnosNotas(lista)
            print ("")
           # operacion()
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu=="4":
            DefinitivaAlumno(lista)
            print ("")
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")

        elif opcionMenu=="5":
            promedioClase(listaDefinitiva)
            print ("")
            input("Has pulsado la opción 5...\npulsa una tecla para continuar")
        
        elif opcionMenu=="5":
            alumnoMayorNota(listaDefinitiva)
            print ("")
            input("Has pulsado la opción 5...\npulsa una tecla para continuar")


        elif opcionMenu=="6":
            print("Chao Chao")
            break

        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    print("Hola mundo hasta luego")

main()