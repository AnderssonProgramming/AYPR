def pedir_datos():
    n=-1
    while n<0:
        n=int(input("Ingrese la cantidad de términos: "))
    
    return n

def factorial(num):
    fact=1
    for j in range (1, num+1):
        fact=fact*j
    
    return fact

def sumatoria(n):
    suma=0
    for i in range (1,n+1):
        suma=suma+factorial(i)
    
    return suma
def mostrar_datos(suma,n):

    print("El resultado de la sumatoria es: ",suma,"con n=",n)
    
def main(): 

    print("Saludos")
    print("El objetivo es calcular la sumatoria de i=1 hasta n de i!")

    n=pedir_datos()

    suma=sumatoria(n)
    mostrar_datos(suma,n)
main()