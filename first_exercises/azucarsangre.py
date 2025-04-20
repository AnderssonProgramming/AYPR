def main():

    #Saludo

    print("Bienvenido")
    print("Indicar el estado de una persona según el nivel de azúcar en la sangre que reporte")

    #Entrada de datos

    nivel_azucar_sangre=float(input("Ingrese su nivel de azúcar en la sangre en mg/dl:"))

    #Proceso 

    if nivel_azucar_sangre<140:
        print("Su nivel de azúcar en la sangre es normal")

    if(nivel_azucar_sangre>=140) and (nivel_azucar_sangre<=199):
        print("Su nivel de azúcar en la sangre indica prediabetes")

    if (nivel_azucar_sangre>199) and (nivel_azucar_sangre<=200):
        print("Su nivel de azúcar en la sangre indica que está propenso a presentar diabetes")

    if nivel_azucar_sangre>200:
        print("Su nivel de azúcar en la sangre indica diabetes")


    #Despedida

    print("Gracias por usar este servicio")
    print("Tarea finalizada")
                              

main()    
