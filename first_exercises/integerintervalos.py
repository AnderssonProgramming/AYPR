def main():

    #Saludo

    print("Bienvenido")
    print("Averiguar si un número entero e pertenece a la unión de los conjuntos formados por los números que pertenecen a los intervalos (a,b] y [5,c)")


    #Entrada de datos

    a=float(input("Ingrese el primer valor:"))
    b=float(input("Ingrese el segundo valor:"))
    c=float(input("Ingrese el tercer valor:"))
    e=float(input("Ingrese el valor a tomar en cuenta:"))

    #Proceso

    if (e>a and e<=b) or (e>=5 and e<c):
        print("El número entero e pertenece a la unión de los conjuntos formados por ese intervalo")
        
    else :
        print("El número entero e no pertenece a la unión de los conjuntos formados por ese intervalo")

    #DESPEDIDA

    print("Gracias por usar este servicio")
    print("Tarea finalizada")
    
main()                    
                    
