def pedir_datos():

    n1=float(input("Ingrese un número: "))
    n2=float(input("Ingrese otro número: "))

    return [n1,n2]

def suma_datos(n1,n2):

    suma=n1+n2

    return suma 

def mostrar_datos(n1,n2,suma):

    print("La suma de",n1,"y",n2,"es: ",suma)
    
def main():
    [n1,n2]=pedir_datos()
    sum=suma_datos(n1,n2)
    mostrar_datos(n1,n2,sum)

main()