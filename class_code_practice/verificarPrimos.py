def main():
    n=int(input("Digite la cantidad de números para satisfacer lo propuesto: "))
    cont=1
    contPrimos=0

    while cont<=n:
        numero=int(input("Ingrese número por número: "))
        if numero % cont!=0:
            contPrimos+=1
        cont=cont+1

    print(f"La cantidad de números primos es {contPrimos}")

main()