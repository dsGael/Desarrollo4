def lee_archivo(archivo:str):
    palabras=[]
    data=[]
    with open(archivo, 'r', encoding="utf-8") as file:
        data = file.readlines()
        for palabra in data:
            palabra=palabra.strip("\n")
            palabras.append(palabra)
    return palabras

if __name__ == "__main__":
    print(lee_archivo("ahorcado/palabras.txt"))

    