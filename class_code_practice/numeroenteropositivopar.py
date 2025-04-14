def main():
    #Saludo
    print("Bienvenido")
    print("Verificar si un número entero positivo es par ")

    #Entrada de datos
    respuesta="SI"
    while respuesta=="SI" or respuesta=="si" or respuesta=="Si":
        numero=int(input("Digite número: "))
        if numero>0:
            if numero%2==0:
                print("El número es par")
                respuesta="No"
            else:
                print("El número es impar")
        
        else:
            print("El número ingresado es negativo o cero")
            respuesta=input("¿Quiere volver a intentarlo: ")
    
    print("Espero haberte servido")

main()