def main():
    n = int(input("Ingrese la cantidad de personas: "))

    if n <= 0:
        print("La cantidad de personas debe ser mayor que 0.")
    else:
        cont = 1
        mayor = 0
        menor = 999

        while cont <= n:
            edad = int(input(f"Ingrese la edad de la persona {cont}: "))
            if edad > mayor:
                mayor = edad
            if edad < menor:
                menor = edad
            cont += 1

    print(f"La persona de mayor edad tiene {mayor} años.")
    print(f"La persona de menor edad tiene {menor} años.")
main()
