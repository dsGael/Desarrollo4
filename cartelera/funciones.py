import csv
from datetime import datetime

def carga_csv(archivo:str) ->list :
    """
    Cargar el csv y regresar una lista
    """
    lista = []
    with open(archivo,'r',encoding='utf-8') as csv_file:
        lista = list(csv.DictReader(csv_file))
        return lista

def peliculas_mas_recientes(lista_peliculas:list) -> list:
    """
    Regresa una lista con las peliculas más recientes
    """
    
    hoy=datetime.now()
    for pelicula in lista_peliculas:
        estreno=pelicula['fecha_estreno']
        estreno=datetime.strptime(estreno,'%Y/%m/%d')
        diferencia=hoy-estreno
        pelicula['dias_desde_estreno']=diferencia.days
    lista_peliculas.sort(key=lambda x:x['dias_desde_estreno'])
    sub_lista=lista_peliculas[:5]
    return sub_lista

def crea_diccionario_peliculas(lista_peliculas:list)->dict:
    d={}
    for pelicula in lista_peliculas:
       k= pelicula['id']
       d[k]=pelicula
    return d



if __name__=="__main__":
    lista = carga_csv('cartelera/cartelera_2024.csv')
    #recientes=peliculas_mas_recientes(lista)
  #  for pelicula in recientes:
   #     print(pelicula['titulo'],pelicula['fecha_estreno'],pelicula['dias_desde_estreno'])
    diccionario=crea_diccionario_peliculas(lista)
    print(diccionario['Dune2'])