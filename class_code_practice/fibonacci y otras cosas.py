#PRIMER PROGRAMA
def pedir_datos():
    n = int(input("Digite la cantidad de términos: "))
    return n

def fibonacci_recursivo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def main():
    n = pedir_datos()
    
    # Mostrar la serie de Fibonacci
    print("Serie de Fibonacci:")
    for i in range(n):
        print(fibonacci_recursivo(i), end=" ")

main()

#PRIMER PROGRAMA SEGUNDA PARTE
# def pedir_datos():
#     n = int(input("Digite la cantidad de términos: "))
#     return n

# def fibonacci_recursivo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fibonacci_recursivo(n+1))/fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# def main():
#     n = pedir_datos()
    
#     # Mostrar la serie de Fibonacci
#     print("Serie de Fibonacci:")
#     for i in range(n):
#         print(fibonacci_recursivo(i), end=" ")

#SEGUNDO PROGRAMA
def pedir_datos():
    n = int(input("Digite el índice del término que desea ver en la serie de Fibonacci: "))
    return n

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def main():
    indice = pedir_datos()
    
    # Calcular el término específico de la serie de Fibonacci
    resultado = fibonacci_recursivo(indice)
    
    # Mostrar el resultado
    print("El término en la posición", indice, "de la serie de Fibonacci es:", resultado)

main()

#TERCER PROGRAMA
def suma(lista):
	if len(lista) == 1: # Caso base
		return lista[0]
	else:
		return lista[0] + suma(lista[1:]) # La función se llama a si misma (Recursión)
# lista[1:] devuelve la lista sin su primer elemento
print(suma([6,3,4,2,10]))

#CUARTO PROGRAMA
def maximo_comun_divisor(a, b):
    if b == 0:
        return a
    else:
        print("maximo_comun_divisor(",b ,",", a%b)
  
        return maximo_comun_divisor(b , a%b)
#     while a%b !=0:
#        b=a%b
#         a=b
# return b

def main():
    a=5
    b=3
    mcd=maximo_comun_divisor(a, b)
    print(mcd)
main()



def pedir_datos():
    a=int(input("Digite un número: "))
    b=int(input("Digite un número: "))

    return [a,b]

def mcd(a,b):
    
    if b>a:
        return mcd(b,a)
    if b==0:
        print ("El algoritmo de Euclides termina!")
        print ("¡El máximo común divisor es",a)
        return a
    else:
        q, r= divmod(a,b)
        print(a,"=",q,"*",b,"+",r)
        print ("mcd(",a,",",b,")=mcd(",b,",",r,")")
        return mcd(b,r)

def main():
    [a,b]=pedir_datos()
    mcd(a,b)
main()