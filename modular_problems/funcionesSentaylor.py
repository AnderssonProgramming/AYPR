def pedir_datos():
    x=float(input("Digite cualquier número: "))
    n=int(input("Ingrese la cantidad de términos: "))

    return[x,n]

def término(x,n):
    cont=1
    expo_fact=1
    senx=0

    while cont <= n:
        contFact=1
        factorial=1

        while contFact <= expo_fact:
            factorial=factorial*contFact
            contFact=contFact+1

        exponente=x**expo_fact
        expo_fact=expo_fact+2

        término=exponente/factorial

        if cont %2==0:
            senx=senx-término
        else:
            senx=senx+término
        cont=cont+1

    print("El sen de x con x= ",x,"y",n,"términos es",senx)

def main():
    [x,n]=pedir_datos()
    término(x,n)
    
   
    
main()