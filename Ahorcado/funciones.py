import random

def lee_archivo(archivo:str):
    palabras = []
    with open(archivo,"r",encoding="utf-8") as a:
        data = a.readlines()
    for palabra in data:
        palabra = palabra.strip("\n")
        palabras.append(palabra)
    return palabras

def palabra_a_diccionario(palabra:str)->list:
    ''' convierte palabra en un diccionario de letras'''
    lista = [ {letra:"_"} for letra in palabra ]
    return lista

def checa_si_gano(lista_letras:list):
    '''[ {'g':'g'},{'a':'a'},{'t':'t'},{'o':'_'}]
    '''
    existe_underscore=False
    for diccionario in lista_letras:
        for k,v in diccionario.items():
            if v == '_':
                existe_underscore=True
    if existe_underscore==True:
        gana = False
    else:
        gana = True
    return gana


if __name__ == "__main__":
    palabras = lee_archivo("palabras.txt")
    print(palabras)
    palabra = random.choice(palabras)
    dp = palabra_a_diccionario(palabra)
    print(dp)
    gat_ = [ {'g':'g'},{'a':'a'},{'t':'t'},{'o':'_'}]
    gato = [ {'g':'g'},{'a':'a'},{'t':'t'},{'o':'o'}]
    print(checa_si_gano(gat_))
    print(checa_si_gano(gato))
