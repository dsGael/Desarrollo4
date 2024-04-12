import unicodedata
from flask import Flask, render_template, request
from funciones import carga_csv, peliculas_mas_recientes
from funciones import crea_diccionario_peliculas
from funciones import crea_diccionario_genero
import os

archivo_cartelera = 'cartelera/cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas=crea_diccionario_peliculas(cartelera)
diccionario_generos = crea_diccionario_genero(cartelera)

@app.route("/")
def index():
    global cartelera
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template("index.html",lista=lista_peliculas)

@app.route("/generos")
def generos():
    return render_template("generos.html",dicc_generos=diccionario_generos)

@app.route("/genero/<id>")
def generos_id(id:str):
    peliculas_por_genero = []
    if id in diccionario_generos:
        for pelicula in cartelera:
            keys = pelicula["genero"]
            keys = unicodedata.normalize('NFD', keys).encode('ascii', 'ignore').decode('utf-8') #quita acentos
            keys = keys.upper()
            keys = keys.split(",")
            for key in keys:
                key = key.strip()
                if key == id:
                    peliculas_por_genero.append(pelicula)
    print(peliculas_por_genero)
    return render_template("genero.html",genero=id,peliculas_por_genero=peliculas_por_genero)
    

@app.route("/anio")
def anio():
    return render_template("anio.html")

@app.route("/alfabetico")
def alfabetico():
    return render_template("alfabetico.html")

@app.route("/pelicula/<id>")
def pelicula(id:str):
    if id in diccionario_peliculas:
        pelicula = diccionario_peliculas[id]  
        print(f"movie={pelicula['titulo']}")  
        return render_template("movie.html",movie=pelicula)
    else:
        return render_template("no_existe.html")
    
if __name__ == "__main__":
    app.run(debug=True)