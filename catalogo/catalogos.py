import csv
import os 
import argparse


class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
        self.area=set()
    
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
    with open(file_path, newline='', encoding='latin1') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def main(folder:str, search_keys:list):
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
    #print(f"Número de llaves en diccionario:{len(diccionario.keys())}")
    #print(f"Revista 'acta':",diccionario['acta'])
    lista=search_keywords(diccionario,search_keys)
    print(f"Resultado:")
    for revista in lista:
        print(revista)


def agregar_revista_diccionario(dic:dict,revista:Revista):
    titulo = revista.titulo
    lista_palabras = titulo.split(" ")
    lista_palabras.append(titulo)
    for palabra in lista_palabras:
        if palabra not in dic:
            dic[palabra] = [revista]
        else:
            dic[palabra].append(revista)

def search_keywords(dictionary:dict,keys:list):
    values= [set(dictionary.get(key,[])) for key in keys]
    if not values:
        return []
    intersection =values[0]
    for value in values[1:]:
        intersection &=value
    return list(intersection)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Procesa archivos csv y genera catálogo'
    )
    parser.add_argument('folder_path',
                        type=str,
                        help='Ruta de la carpeta con csvs'
                        )
    parser.add_argument("search_keys",metavar="K",type=str,nargs="+",)
    args = parser.parse_args()
    folder_path = args.folder_path
    keys=args.search_keys
    main(folder_path, keys)