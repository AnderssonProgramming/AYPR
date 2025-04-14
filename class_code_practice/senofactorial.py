def main():
    n=int(input("Ingrese la cantidad de términos: "))
    x=float(input("Ingrese el valor a tener en cuenta: "))
    cont=0
    factorial=1
    while cont<n:
        
        numerador= x**(2*cont)*(2*cont+1)
        denominador= factorial

        if cont%2==0:
            cont=cont*-1
          
        else: 
            cont=cont*1 
        
        cont+=1
        

    division=(x**factorial)/denominador
    print(division)
    senx=division
    
    print(senx)
    
main()