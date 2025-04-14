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

    cont=1
    expo_facto=1
    senx=0

    while cont <= n:

    #Factorial
        contfact=1
        factorial=1
        while contfact <= expo_facto:
            factorial=factorial*contfact
            contfact=contfact+1

    #Exponente
        exponente=x**expo_facto

        expo_facto=expo_facto+2

    #Término
        termino=exponente/factorial
        print("Término",cont,"es: ",exponente,"/",factorial)

    #Signo
        if cont%2==0:
            senx=senx - termino
        
        else:
            senx=senx + termino

        cont=cont+1
    
    print("La suma es: ",senx)

main()