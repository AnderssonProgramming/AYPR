"""
ASIGNATURA: Algoritmos y programación de computadores
OBJETIVO: El objetivo es formar una palabra con los caracteres que se encuentran en las posiciones pares del vector
AUTOR(ES): Andersson David Sánchez Méndez
FECHA: 27/09/23
"""

MAX=50
def pedir_tamaño():
    tam=-1
    while tam <=0 or tam > MAX:
        tam=int(input("Dame el tamaño: "))
    
    return tam

def crear_vector():
    vec_caracteres=["-" for i in range (0,MAX)]
    return vec_caracteres

def llenar_vector(tam,vec_caracteres):

    for pos in range (0,tam):
        vec_caracteres[pos]=input("Digite carácter: ")

def armar_y_mostrar_pal(tam,vec_caracteres):

    for pos in range (0,tam):
    #for pos in range (0,tam,2)
        if pos%2==0:
            print(vec_caracteres[pos],end= " ")
def main():
    print("Bienvenido")
    print("El objetivo es formar una palabra con los caracteres que se encuentran en las posiciones pares del vector")
    tam=pedir_tamaño()
    vec_caracteres=crear_vector()
    llenar_vector(tam,vec_caracteres)
    armar_y_mostrar_pal(tam,vec_caracteres)
    print("Chao chao")

main()