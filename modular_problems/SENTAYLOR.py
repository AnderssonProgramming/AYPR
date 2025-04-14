"""
ASIGNATURA: Algoritmos y programación de computadores
OBJETIVO: Mostrar el resultado del sen x usando la serie de Taylor, pidiendo al usuario un valor x y la cantidad de términos n (más cantidad significa resultados más precisos)
AUTOR(ES): Andersson David Sánchez Méndez
FECHA: 11/09/23
"""

def main():

    #Saludo

    print("Bienvenido")
    print("Mostrar el resultado del sen x usando la serie de Taylor, pidiendo al usuario un valor x y la cantidad de términos n (más cantidad significa resultados más precisos)")

    #Entrada de datos

    x = float(input("Ingrese el valor de x en radianes: "))
    n = int(input("Ingrese la cantidad de términos a calcular: "))

    senx = 0
    cont = 0
    signo = 1
    factorial = 1

    #Proceso

    while cont < n:
        numerador = x ** (2 * cont + 1)
        denominador = factorial

    #Determinar el signo 

        if signo == 1:
            senx = senx + (numerador / denominador)

        else:
            senx = senx- (numerador / denominador)
        
        print("Término",cont, "es", numerador,"/",denominador)

        signo = signo * -1
        cont = cont + 1 #Contador cantidad términos suma
        factorial = factorial * (2 * cont) * (2 * cont + 1)

    print("El valor aproximado de sinx es,",senx, "con x igual a",x, "y la cantidad de términos",n)
    print("Espero haberte servido")

main()