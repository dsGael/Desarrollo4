import csv
import os 
import argparse


class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
        self.area = set()
    
    def __str__(self):
        return f'{self.titulo} - {self.catalogos} - {self.area}'

    def __repr__(self):
        return f'{self.titulo} - {self.catalogos} - {self.area}'
    
    def addArea(self,area:str):
        self.area.add(area)

def read_folder(folder_path:str) -> list:
    return os.listdir(folder_path)

def extract_left_of_underscore(strings:list) -> list:
    return [string.split("_")[0] for string in strings]

def read_csv(file_path:str) -> list:
    with open(file_path, newline='',encoding='latin1') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def agregar_revista_diccionario(dic:dict,revista:Revista):
    titulo = revista.titulo
    lista_palabras = titulo.split(" ")
    lista_palabras.append(titulo)
    for palabra in lista_palabras:
        if palabra not in dic:
            dic[palabra] = [revista]
        else:
            dic[palabra].append(revista)

def search_keywords(dictionary:dict, keys:list):
    """
    Find the intersection of values
    """
    values = [set(dictionary.get(key,[])) for key in keys]
    if not values:
        return []
    intersection = values[0]
    for value in values[1:]:
        intersection &= value
    return list(intersection)

def agrega_revistas_a_dict(dic:dict,lista_revistas,area):
    for titulo in lista_revistas:
        titulo = titulo[0] #primer elemento de la lista
        if titulo in dic:
            dic[titulo].append(area)
        else:
            dic[titulo] = [area]

def procesa_areas(folder:str)-> dict:
    files_list = read_folder(folder)
    files_list = [file for file in files_list if file.endswith('.csv')]
    diccionario = {}
    for files in files_list:
        filename = os.path.join(folder,files)
        titulos = read_csv(filename) #leyendo los titulos
        area = files.split(" ")[0] #extraemos nombre del area
        agrega_revistas_a_dict(diccionario,titulos,area)
    return diccionario

def asigna_areas_a_revistas(d_revistas:dict, d_areas:dict):
    for titulo, revista in d_revistas.items():
        for r in revista:
            if r.titulo in d_areas.keys():
                areas = d_areas[r.titulo]
                #print(f"revista:{type(revista)} : {revista}")
                r.addArea=(areas[0])
               


def main(folder:str, folder_areas:str, keys:list):
    files_list = read_folder(folder)
    files_list = [file for file in files_list if file.endswith('.csv')]
    catalogo_list = extract_left_of_underscore(files_list)
    print(catalogo_list)
    lista_revistas = []
    diccionario = {}
    for files in files_list:
        filename = os.path.join(folder,files)
        titulos = read_csv(filename) #leyendo los titulos
        catalogo = files.split("_")[0] #extraemos nombre del catalogo
        for titulo in titulos:
            titulo = titulo[0]
            titulo = titulo.lower()
            revista = Revista(titulo,catalogo)
            #agregar revista al diccionario
            agregar_revista_diccionario(diccionario,revista)
    dicc_areas = procesa_areas(folder_areas)
    asigna_areas_a_revistas(diccionario,dicc_areas)
    print(f"Número de llaves en diccionario:{len(diccionario.keys())}")
    #print(f"Revista 'acta':",len(diccionario['acta']))
    #print(f"Revista 'universitaria':",len(diccionario['universitaria']))
    lista = search_keywords(diccionario,keys)
    print("Resultado:")
    for revista in lista:
        print(revista)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Procesa archivos csv y genera catálogo'
    )
    parser.add_argument('folder_path',
                        type=str,
                        help='Ruta de la carpeta catalogos con csvs'
                        )
    parser.add_argument('folder_areas',
                        type=str,
                        help='Ruta de la carpeta areas con csvs'
                        )
    parser.add_argument("search_keys",
                        metavar="K",
                        type = str,
                        nargs ="+",
                        help ="")
    #args = parser.parse_args()
   # folder_path = args.folder_path
   # folder_areas = args.folder_areas
    #search_keys = args.search_keys
  
    folder_path="./catalogo/datos/catalogos/"
    folder_areas="./catalogo/datos/areas/"
    search_keys = ["acta", "geophysica"]
    main(folder_path, folder_areas, search_keys)