"""
ASIGNATURA: Algoritmos y programación de computadores
OBJETIVO: El objetivo es determinar cuántas veces está un número entero en un vector de tamaño dado
AUTOR(ES): Andersson David Sánchez Méndez
FECHA: 27/09/23
"""

MAX=100

def pide_cantidad():
    n=0
    while n <=0 or n> MAX:
        n=int(input("Digite tamaño: "))
        nInt=float(input("Digite un número real: "))
    return [n,nInt]

def crear_vector():
    vector_numeros=[0 for i in range (MAX)]
    return vector_numeros

def llenar_vector(vector_numeros,n):

    for pos in range (0,n):
        vector_numeros[pos]=int(input("Digite número: "))

def contnum(vector_numeros,n,nInt):

    contnum=0

    for i in range (0,n):
        if vector_numeros[i] ==nInt:
            contnum=contnum+1
    
    return contnum

def mostrar_vector(vector_numeros,n):
    print("Los datos del vector son: \n")
    for pos in range (0,n):
        print (vector_numeros[pos],end = " ")

def mostrar_datos(vector_numeros,n,nInt,contn):
    mostrar_vector(vector_numeros,n)
    print("La cantidad de veces que está el número ingresado es: ",contn,"con tamaño=",n,"y su número entero=",nInt)

def main():
    print("Bienvenido")
    print("El objetivo es determinar cuántas veces está un número entero en un vector de tamaño dado")
    [n,nInt]=pide_cantidad()
    vector_numeros=crear_vector()
    llenar_vector(vector_numeros,n)
    contn=contnum(vector_numeros,n,nInt)
    mostrar_datos(vector_numeros,n,nInt,contn)
    print("Chao chao")

main()