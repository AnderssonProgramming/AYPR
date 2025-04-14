def pedir_datos():

    E=-1

    while E < 0:
        E=int(input("Ingrese cuántos estudiantes hay: "))

    return E

def edad_sexo_cantidadAsig_carrera(E):
    cont=1
    while cont <=E:
        edad=int(input("Ingrese su edad: "))
        sexo=int(input("Digite 0 si su sexo es femenino o 1 si es masculino: "))
        cantidadAsig=int(input("Ingrese cuántas asignaturas está cursando: "))
        carrera=input("Digite ic si su carrera es ingeniería civil, ie para ingeniería eléctrica, is para ingeniería de sistemas, ii para ingeniería industrial, il para ingeniería electrónica y ec para economía: ")

        contH=0
        if edad < 18 and sexo==1:
            contH=contH+1
        
            

        contM=0
        if edad >= 18 and sexo==0:
            contM=contM+1
            
           
        edadmH=-1
        carreramH=""
        if sexo==1 and edad < edadmH:
            edadmH=edad
            carreramH=carrera

           
        edadMM=1000
        carreraMM=""
        if sexo==0 and edad>edadMM:
            edadMM=edad
            carreraMM=carrera


        total_asignaturas=0
        
        total_asignaturas=total_asignaturas + cantidadAsig
        
        cont=cont+1
    
    promedio=total_asignaturas/E
    
    print("Estos datos fueron a partir de",E,"estudiantes")
    print("El número de hombres con menos de 18 años es: ",contH)
    print("El número de mujeres con 18 o más años es: ",contM)
    print("La edad y carrera del menor de los hombres es: ",edadmH,"y estudia",carreramH)
    print("La edad y carrera de la mayor de las mujeres es: ",edadMM,"y estudia",carreraMM) 
    print("El promedio de asignaturas que cursan los estudiantes, sin importar el sexo, edad ni carrera es: ",promedio)
    
def main():
    E=pedir_datos()
    edad_sexo_cantidadAsig_carrera(E)
   
main()