import random



def main():
    
    ciudades=['Bogota', 'Barranquilla', 'Cali', 'Medellín', 'Bucaramanga', 'Pasto', 'Cartagena']
    regiones=['Caribe', 'Centro', 'Sur']
    partidos=['Partido1', 'Partido2', 'Partido3']
    candidatos=['Candidato1', 'Candidato2', 'Candidato3', 'Candidato4']
    sitios=['Sitio1', 'Sitio2','Sitio3']
    mesas=['Mesa1', 'Mesa2', 'Mesa3', 'Mesa4']
    genero=['Hombre','Mujer']


#Candidato,partido,ciudad,sitio,mesa,genero
    
    archivo = open("votacion1.txt",'a')
    for cant in range(50):
        
        linea= random.choice(candidatos)+","+ random.choice(partidos)+ ","+ random.choice(ciudades)+ "," + random.choice(sitios) + "," + random.choice(mesas)  + "," + random.choice(genero) 
        print(linea)
        archivo.write(linea)
        archivo.write("\n")
    archivo.close()
    
main()