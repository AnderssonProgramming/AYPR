def main():

    #Saludo

    print("Bienvenido")
    print("Mostrar el pago que le corresponde al usuario")

    #Entrada de datos

    nombre_usuario=input("Ingrese su nombre:")
    horas_trabajadas=float(input("Ingrese su número de horas trabajadas:"))
    valor_hora=float(input("Ingrese su valor por hora en dólares ($):"))

    #Proceso

    pago=horas_trabajadas*valor_hora
    print("Su pago es de:$",pago)

    #Despedida

    print("Gracias por usar este servicio",nombre_usuario)
    print("Tarea finalizada")
    
main()
