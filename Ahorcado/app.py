from flask import Flask, render_template,request
from os import path
from funciones import lee_archivo
import random


app=Flask(__name__)

palabras=lee_archivo("Ahorcado/palabras.txt") 
conteo=0
abc="ABCDEFGHIJKLMNOPQSTUVWXYZ"

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='GET':
       # print(app.url_map)
        palabra=random.choice(palabras)
        print(palabra)
        image=f"/static/images/monito-{conteo}.png"
        letras=[{'letra':x, 'id_letra':x}for x in abc]
        listado=[(d['letra'],d['id_letra']) for d in letras]
        return render_template('index.html', imagen=image, abecedario=abc, lista_abc=listado)



    
if __name__=='__main__':
    app.run(debug=True)
