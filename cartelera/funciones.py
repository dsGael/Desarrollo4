import csv

def carga_csv(nombre_archivo:str)->list:
    lista=[]
    with open(nombre_archivo,'r',encoding='utf-8') as archivo:
        lista=list(csv.DictReader(archivo))
    return lista

if __name__ == '__main__':
    print(carga_csv('cartelera/cartelera_2024.csv'))