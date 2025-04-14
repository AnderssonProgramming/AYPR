def main():
    #Saludo
    # print("Bienvenido")
    # print("Dada una cantidad de números, encontrar el mayor de esos números enteros")

    # #Entrada de datos
    # n=int(input("Ingrese la cantidad de números: "))
    # mayor=int(input("Digite el número a revisar: "))
    # cont=1
    # while cont<n:
    #     numero=int(input("Ingrese número por número: "))
    #     if numero>mayor:
    #         mayor=numero
    #     cont+=1
    
    # print("El número mayor es",mayor)
    # #Entrada de datos
    n=int(input("Ingrese la cantidad de números: "))
    numero=int(input("Ingrese número por número: "))
    mayor=numero
    cont=1
    while cont<n:
        numero=int(input("Ingrese número por número: "))
        if numero>mayor:
            mayor=numero
        cont+=1
    
    print("El número mayor es",mayor)


main()