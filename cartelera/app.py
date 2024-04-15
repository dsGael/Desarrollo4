from flask import Flask, render_template
from funciones import carga_csv, peliculas_mas_recientes
from funciones import crea_diccionario_peliculas
from funciones import crea_diccionario_genero
from funciones import crea_diccionario_años
from funciones import crea_diccionario_alfabetico

archivo_cartelera = 'cartelera/cartelera_2024.csv'
app = Flask(__name__)
cartelera = carga_csv(archivo_cartelera)
diccionario_peliculas=crea_diccionario_peliculas(cartelera)
diccionario_generos = crea_diccionario_genero(cartelera)
diccionario_años = crea_diccionario_años(cartelera)
diccionario_letras = crea_diccionario_alfabetico(cartelera)

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
        peliculas_por_genero=diccionario_generos[id]
    return render_template("genero.html",genero=id,peliculas_por_genero=peliculas_por_genero)
    

@app.route("/anios")
def anio():
    print(diccionario_años)
    return render_template("anios.html", dicc_anio=diccionario_años)

@app.route("/anio/<id>")
def anio_id(id:str):
    peliculas_por_año = []
    if id in diccionario_años:
        peliculas_por_año=diccionario_años[id]
    
    return render_template("anio.html",anio=id,peliculas_por_año=peliculas_por_año)

@app.route("/letras")
def alfabetico():
    return render_template("letras.html", dicc_letra=diccionario_letras)

@app.route("/letra/<id>")
def alfabetico_id(id:str):
    peliculas_por_letra = []
    if id in diccionario_letras:
       peliculas_por_letra=diccionario_letras[id]
    
    return render_template("letra.html",letra=id,peliculas_por_letra=peliculas_por_letra)

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