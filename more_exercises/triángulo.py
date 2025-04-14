"""ANDERSSON DAVID SÁNCHEZ MÉNDEZ"""
def main():

    #Saludo

    print("Bienvenido")
    print("Mostrar que tres longitudes conformen un triángulo, mirar qué tipo de triángulo es. Si es EQUILÁTERO, se debe realizar la suma de sus tres lados; si es ESCALENO, debe mostrar la medida del lado menor y si es ISÓSCELES, debe calcular la diferencia entre el producto de los dos lados iguales y el otro lado")

    #Entrada de datos

    lado1=float(input("Ingrese la primera longitud del triángulo:"))
    lado2=float(input("Ingrese la segunda longitud del triángulo:"))
    lado3=float(input("Ingrese la tercera longitud del triángulo:"))
    suma=lado1+lado2+lado3
    producto_diferencia1=(lado1*lado2-lado3) 
    producto_diferencia2=(lado2*lado3-lado1)
    producto_diferencia3=(lado1*lado3-lado2)

    #Verificación del triángulo
    
    if (lado1 or lado2 or lado3)>0:

        if lado1+lado2>lado3 and lado2+lado3>lado1 and lado1+lado3>lado2:
            
            if lado1+lado2>lado3 and lado2+lado3>lado1 and lado1+lado3>lado2:
                print("Las tres longitudes conforman un triángulo")

            #Tipo de triángulo
            if lado1==lado2==lado3:
                tipo_triángulo="Equilátero"
        
            else:
                if ((lado1==lado2) and (lado1!=lado3)) or ((lado2==lado3) and (lado2!=lado1)) or ((lado1==lado3) and (lado1!=lado2)):
                    tipo_triángulo="Isósceles"
            
                else:
                    tipo_triángulo="Escaleno"
    
            #Proceso para cada tipo de triángulo

            if tipo_triángulo=="Equilátero":
                print("Es un triángulo equilátero con suma de sus longitudes igual a",suma)
        
            if tipo_triángulo=="Isósceles":

                if ((lado1==lado2) and (lado1!=lado3)):
                    print("Es un triángulo isósceles con producto de las longitudes iguales menos la faltante",producto_diferencia1)
            
                else:
                    if ((lado2==lado3) and (lado2!=lado1)):
                        print("Es un triángulo isósceles con producto de las longitudes iguales menos la faltante",producto_diferencia2)
                
                    else:
                        if ((lado1==lado3) and (lado1!=lado2)):
                            print("Es un triángulo isósceles con producto de las longitudes iguales menos la faltante",producto_diferencia3)
                        else:
                            print("")
    
            if tipo_triángulo=="Escaleno":

                if lado1<lado2 and lado1<lado3:
                    print("Es un triángulo escaleno con lado menor de:",lado1)
                else:
                    if lado2<lado3 and lado2<lado1:
                        print("Es un triángulo escaleno con lado menor de:",lado2)
                    
                    else:
                        if lado3<lado1 and lado3<lado2:
                            print("Es un triángulo escaleno con lado menor de",lado3)
                        else:
                            print("")

        else:
            print("Las tres longitudes no conforman un triángulo")            
    else:
        print("Intente de nuevo.No se aceptan números negativos")
    
    #Despedida

    print("Gracias por usar este servicio")
    print("Tarea finalizada")


main()