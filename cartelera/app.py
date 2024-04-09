from flask import Flask, render_template, request
from funciones import carga_csv, peliculas_mas_recientes

app = Flask(__name__)
cartelera=carga_csv('cartelera/cartelera_2024.csv')

@app.route('/')
def index():
    global cartelera
    lista_peliculas = peliculas_mas_recientes(cartelera)
    return render_template('index.html', lista=lista_peliculas)

@app.route('/generos')
def generos():
    return render_template('generos.html')

@app.route('/anio')
def anio():
    return render_template('anio.html')

@app.route('/alfabetico')
def alfabetico():
    return render_template('alfabetico.html')
@app.route('/pelicula')
def pelicula():
    return render_template('pelicula.html')


if __name__ == '__main__':
    app.run(debug=True)