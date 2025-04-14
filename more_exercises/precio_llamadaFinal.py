"""ANDERSSON DAVID SÁNCHEZ MÉNDEZ"""
def main():
    
    #Saludo
    print("Bienvenido")
    print("Calcular el precio total de la llamada")

    #Entrada de datos

    tiempo=float(input("Ingrese su tiempo de llamada en minutos (min):"))
    if tiempo>0:
        día=input("Ingrese el día de la llamada:")
        if día=="Domingo":
            print("")
        else:
            turno=input("Ingrese su turno(Mañana o Tarde):")


    #Encontrar la base
    

        if tiempo>0 and tiempo<=5:
            base=tiempo*1

        else:
            if tiempo>5 and tiempo<=8:
             base=tiempo*1.8

            else:
                if tiempo>8 and tiempo<=10:
                    base=tiempo*2.5

                else:
                    base=tiempo*3.0

    #Encontrar el impuesto

        if día=="Domingo":
            impuesto=0.03*base

        else:
            if turno=="Mañana":
                impuesto=0.15*base

            else:
                impuesto=0.10*base

        print("Usuario, si su tiempo de llamada fue de",tiempo,"min, el precio base será de",base, "euros e impuesto",impuesto,"euros, entonces el precio total de su llamada es:",base+impuesto,"euros")

    else:
        print("Intente de nuevo")
    
main()
