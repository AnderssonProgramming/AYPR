"""
ASIGNATURA: Algoritmos y programación de computadores
OBJETIVO: El objetivo es encontrar el vector suma que se forma de sumar correspondientemente cada casilla de los dos vectores dados.
AUTOR(ES): Andersson David Sánchez Méndez
FECHA: 27/09/23
"""

MAX=100

def pide_cantidad():
    n=-1
    while n <=0 or n> MAX:
        n=int(input("Digite tamaño: "))
    return n

def crear_vector(n):
    vector_numeros=[0 for i in range (n)]
    return vector_numeros

def llenar_vectores(vector1,vector2,vectorSuma,n):
    llenar_vector(vector1,"primer",n)
    llenar_vector(vector2,"segundo",n)
    llenar_vector_suma(vector1,vector2,vectorSuma,n)

def llenar_vector(vector,numV,n):
    for pos in range(0,n):
        print("Por favor ingresa real #",pos+1," del",numV,"vector:") 
        vector[pos]= float(input(""))

def llenar_vector_suma(vector1,vector2,vectorSuma,n):
    for pos in range(0,n):
        vectorSuma[pos] = vector1[pos] + vector2[pos]


def mostrar_datos(n,vector1,vector2,vectorSuma):

    print("Estimado usuario, el vector suma de los dos vectores de tamaño ",n," es de la siguiente manera")
    print("\n|#Elemento| = |Vector 1| + |Vector 2| = |Vector3|")

    for pos in range(0,n):
        print("\n#",pos+1,"         |",vector1[pos],"|  +  |",vector2[pos]," | =   | ",vectorSuma[pos],"|")

def main():
    print("Bienvenido")
    print("El objetivo es encontrar el vector suma que se forma de sumar correspondientemente cada casilla de los dos vectores dados.")
    n=pide_cantidad()
    vector_numeros1=crear_vector(n)
    vector_numeros2=crear_vector(n)
    vector_suma=crear_vector(n)
    llenar_vectores(vector_numeros1,vector_numeros2,vector_suma,n)
    mostrar_datos(n,vector_numeros1,vector_numeros2,vector_suma)
    print("Chao chao")

main()