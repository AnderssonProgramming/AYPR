"""
ASIGNATURA: Algoritmos y programación de computadores
OBJETIVO: El objetivo es calcular la sumatoria de i=1 hasta n de i!
AUTOR(ES): Andersson David Sánchez Méndez
FECHA: 27/09/23
"""
def pide_datos():

    n=-1
    while n<0:
        n=int(input("Ingrese la cantidad de términos: "))
    
    return n

def factorial (num):
    fact=1
    cont=1

    while cont <= num:

        fact=fact*cont
        cont=cont+1
    
    return fact

def sumatoria(n):

    suma=0
    cont=1
    while cont <=n:
        suma=suma+factorial(cont)
        cont=cont+1
    
    return suma

def mostrar_datos(suma,n):

    print("El resultado de la sumatoria es: ",suma,"con n=",n)
    
def main():
    print("Bienvenido")
    print("El objetivo es calcular la sumatoria de i=1 hasta n de i!")
    n=pide_datos()
    suma=sumatoria(n)
    mostrar_datos(suma,n)
    print("Chao chao")
main()