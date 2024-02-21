from Revista import Revista
# Gael Humberto Borchardt Castellanos

def lee_archivo(archivo)->list:
    lista=[]
    with open(archivo,"r",encoding="utf8") as textos:
        for linea in textos:
            titulo=linea.strip().lower()
            lista.append(titulo)
    return lista

def Crear_Lista_Revistas(lista:list[str], catalogo:str)->list:
    lista_Revistas=[]
    for linea in lista:
        r= Revista(titulo=linea,catalogo=catalogo)
        lista_Revistas.append(r)
    return lista_Revistas

def Diccionario_Revistas(lista_Revista:list[Revista])->dict:
    diccionario={}
    for revista in lista_Revista:
        titulo=revista.titulo
        splitteado=titulo.split()
        for i in range(len(splitteado)):
            if splitteado[i] in diccionario:
                diccionario[splitteado[i]].append(revista)
            else:
                diccionario[splitteado[i]]=[revista]
    return diccionario  
   
      
def Buscar_Revista(diccionario:dict, palabra:str)->list:
    if palabra in diccionario:
       print("\n Revistas encontradas: ")
       for revista in diccionario[palabra]:
           print(f"{revista}")
   

def main():
    lista=lee_archivo('Examen_1/CONACYT_RadGridExport.csv')
    lista_Revistas=Crear_Lista_Revistas(lista,"CONACYT")
    diccionario=Diccionario_Revistas(lista_Revistas)
    palabra=input("Ingrese una palabra: ")
    revistas=Buscar_Revista(diccionario,palabra)
    print(f"{revistas}")
    

if __name__ == '__main__':
    main()