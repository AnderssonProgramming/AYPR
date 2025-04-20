def main():

    #Saludo

    print("Bienvenido")
    print("Leer el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado")

    #Entrada de datos

    peso_payaso=input("El peso de cada payaso es de: 112g")
    pesoPayaso=112
    peso_muñeca=input("El peso de cada muñeca es de: 75g")
    pesoMuñeca=75

    cantidadPayasos=int(input("Ingrese la cantidad de payasos vendidos en el último pedido:"))
    cantidadMuñecas=int(input("Ingrese la cantidad de muñecas vendidas en el último pedido:"))

    #Proceso

    peso_total=(pesoPayaso*cantidadPayasos)+(pesoMuñeca*cantidadMuñecas)

    print("El peso total del paquete que será enviado es de:",peso_total,"g")
    
    #Despedida

    print("Agradezco por usar este servicio")
    print("Tarea finalizada")

main()    
