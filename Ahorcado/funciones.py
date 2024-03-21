def lee_archivo(archivo:str):
    palabras=[]
    data=[]
    with open(archivo, 'r', encoding="utf-8") as file:
        data = file.readlines()
        for palabra in data:
            palabra=palabra.strip("\n")
            palabras.append(palabra)
    return palabras

def palabra_toList(palabra:str)-> list:
    lista=[{letra:"_"} for letra in palabra]
    return lista



if __name__ == "__main__":
    print(lee_archivo("ahorcado/palabras.txt"))
    print(palabra_toList("papu"))
    