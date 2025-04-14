def pedir_datos():
    n1=-1 
    n2=-1
    while n1<0:
        n1=int(input("Ingrese un número entero positivo: "))
    while n2<0:
        n2=int(input("Ingrese otro número entero positivo: "))

    return [n1,n2]

def Divisorespropios(numero):
    contD=1
    suma=0
    while contD <= numero//2:
        if numero % contD ==0:
            suma=suma+contD
        
        contD=contD+1
    
    return suma
    

def main():
    [n1,n2]=pedir_datos()
    div_n1=Divisorespropios(n1)
    div_n2=Divisorespropios (n2)

    if div_n1==n2 and div_n2==n1:
        print(n1,"y",n2,"son amigos")
    else:
        print(n1,"y",n2," no son amigos")

    
main()