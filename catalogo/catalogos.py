import csv
import os
import argparse 


class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo = titulo
        self.catalogos = set()
        self.catalogos.add(catalogo)
    
    def __str__(self):
        return f'{self.titulo} - {self.catalogos}'

    def __repr__(self):
        return f'{self.titulo} - {self.catalogos}'

def read_folder(folder_path:str) -> list:
    return os.listdir(folder_path)

def extract_left_of_underscore(strings:list) -> list:
    return [string.split("_")[0] for string in strings]

def read_csv(file_path:str) -> list:
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]

def main(folder:str):
    files_list=read_folder(folder)
    files_list=[file for file in files_list if file.endswith(".csv")]
    catalogo_list=extract_left_of_underscore(files_list)
    print(catalogo_list)
    lista_revistas=[]
    for files in files_list:
        titulos=read_csv(files)
        lista_revistas.append(titulos)

    
if __name__ == "__main__":
    parser=argparse.ArgumentParser(description="Procesa archivos csv y genera catalogo")
    parser.add_argument('folder_path', type=str, help="Ruta de la carpeta con archivos csv")
    args=parser.parse_args()
    folder_path = args.folder_path
    print(folder_path)      