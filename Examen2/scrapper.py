# Gael Humberto Borchardt Castellanos 05/04/2024
import requests
from bs4 import BeautifulSoup
from Revista import Revista
import os 
import argparse

def scrap(URL:str):
    '''
    Scrap the URL
    '''
    page = requests.get(URL)
    return page

def lee_archivo(archivo)->list:
    lista=[]
    with open(archivo,"r",encoding="utf8") as textos:
        for linea in textos:
            titulo=linea.strip().lower()
            lista.append(titulo)
    return lista

def find_table(dom):
    '''
    Find the table in the page
    '''
    table=dom.find('table')
    return table

def get_info(table)->list:
    dict={}
    lista=[]

    table_body=table.find('tbody')

    table_rows=table_body.find_all('tr')

    for row in table_rows:
        row_columns=row.find_all('td')
        i=0
        for renglon in row_columns:
            if i==1: 
                renglon=renglon.find('a')
                titulo=renglon.text.strip()
            if i==2:
                catalogo=renglon.text.strip()
            if i==3:
                sjr=renglon.text.strip()
                sjr=sjr.split()[0]
               
                renglon=renglon.find('span')
                q=renglon.text.strip()
                
            if i==4:
                h_index=renglon.text.strip()
            if i==8:
                total_citas=renglon.text.strip()
            i+=1
        revista= Revista(titulo,catalogo,sjr,q,h_index,total_citas)
        lista.append(revista)

    return lista


def revistas_menores(lista: list[Revista], valor:float)->list:
    '''
    Return the list of the revistas with a sjr less than the value
    '''
    lista_menores=[]
    for revista in lista:
        if revista.h_index<valor:
            lista_menores.append(revista)
    return lista_menores

   

def guardar_json(lista: list[Revista], archivo:str):
    with open(archivo,'w') as file:
        
        for revista in lista:
            file.write(repr(revista)+'\n')
    print(f'Archivo {archivo} guardado')


def revistas_mayores(lista: list[Revista], valor:float)->list:
    '''
    Return the list of the revistas with a sjr greater than the value
    '''
    lista_mayores=[]
    for revista in lista:
        if revista.h_index>valor:
            lista_mayores.append(revista)
    return lista_mayores


def main():
    parser = argparse.ArgumentParser(description='Procesa archivos csv y genera catálogo' )
    parser.add_argument('h_index',type=str,help='index h para filtrar revistas' )
    parser.add_argument('json',type=str,help='json nombre' )
    parser.add_argument('mayor_menor',type=str,help='mayor o menor' )


    lista=lee_archivo('Examen2/urls.txt')
    lista_revT=[]
    #lee todas las listas
    for i in range(len(lista)):
        pagina=scrap(lista[i])
        soup=BeautifulSoup(pagina.content,'html.parser')
        tabla=find_table(soup)
        lista_rev=get_info(tabla)
        h_index=parser.parse_args().h_index
        mayor_menor=parser.parse_args().mayor_menor
        name_json=parser.parse_args().json
        name_json=name_json+'.json'
        if mayor_menor=='mayor':
            revistas=revistas_mayores(lista_rev,int(h_index))
            print("REVISTAS MAYORES AL INDEX "+h_index)
        elif mayor_menor=='menor':
            revistas=revistas_menores(lista_rev,int(h_index))
            print("REVISTAS MENORES AL INDEX "+h_index)
       
        print(revistas)
        lista_revT+=lista_rev

    
    guardar_json(lista_revT, name_json)

if __name__ == '__main__':
    
    main()

