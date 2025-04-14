MAX=15

def pide_cantidad():
    n=0
    while n <=0 or n> MAX:
        print("\nEscribe un número entre 1 y", MAX, end= " ")
        n=int(input(":"))

    return n

def crear_vector():
    vector_numeros=[0 for i in range (MAX)]
    return vector_numeros

def llenar_vector(vector_numeros,n):

    for pos in range (0,n):
        vector_numeros[pos]=int(input("Digite número: "))

def contar_pos(vector_numeros,n):
    contPositivos=0

    for pos in range (0,n):
        if vector_numeros[pos]>0:
            contPositivos=contPositivos+1
    
    return contPositivos

def mostrar_vector(vector_numeros,n):
    print("Los datos del vector son: \n")
    for pos in range (0,n):
        print (vector_numeros[pos],end = " ")

def mostrar_datos(vector_numeros,n,contPositivos):
    mostrar_vector(vector_numeros,n)
    print("La cantidad de elementos positivos ingresados es: ",contPositivos)

def main():
    print("Saludos")
    n=pide_cantidad()
    vector_numeros=crear_vector()
    llenar_vector(vector_numeros,n)
    contPositivos=contar_pos(vector_numeros,n)
    mostrar_datos(vector_numeros,n,contPositivos)
    print("Chao chao")

main()
    