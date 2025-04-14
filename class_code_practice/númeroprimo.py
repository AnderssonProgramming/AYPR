"""
ASIGNATURA: Algoritmos y programación de computadores
OBJETIVO: Verificar si un número positivo dado por el usuario es un número primo
AUTOR(ES): Andersson David Sánchez Méndez
FECHA: 11/09/23
"""

def main():

    #Saludo
    
    print("Bienvenido")
    print("Verificar si un número positivo dado por el usuario es un número primo")

    #Entrada de datos

    numero=int(input("Digite un número: "))
    cont=1
    divisores=0

    #Proceso

    if numero>0:
        while cont<=numero:
            if numero%cont==0:
                divisores=divisores+1
            cont=cont+1

        if divisores<=2 and divisores!=1 :
            print("El número es primo")
        else:
            print("El número no es primo")

    else:
        print("El número ingresado es cero o negativo")
    
    print("Espero haberle servido")
    
main()


#divisores=2
#cont=2
#cont<=numero//2 and bandera=0