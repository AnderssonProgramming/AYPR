def main():

    #Saludo

    print("Bienvenido")
    print("Verificar si el dígito de las centenas es igual al de las unidades")

    #Entrada de datos

    numero=int(input("Ingrese un número de tres (3) cifras:"))

    #Proceso

    if numero % 10 == numero // 100:
        print("Cumple la condición")

    else:
        print("No cumple la condición")

    #Despedida

    print("Gracias por usar este servicio")
    print("Tarea finalizada")
main()
