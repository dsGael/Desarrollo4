from flask import Flask, render_template,request
from os import path
from funciones import lee_archivo, palabra_toList
import random


app=Flask(__name__)
conteo=0
palabras=lee_archivo("Ahorcado/palabras.txt") 
abc="abcdefghijklmnopqrstuvwxyz"

@app.route('/', methods=['GET','POST'])
def index():
    global conteo
    global palabraL
    global listado
     
    if request.method=='GET':
        palabra=random.choice(palabras)
        palabraL=palabra_toList(palabra)
        image=f"/static/images/monito-{conteo}.png"
        letras=[{'letra':x, 'id_letra':x}for x in abc]
        listado=[(d['letra'],d['id_letra']) for d in letras]
        return render_template('index.html', imagen=image, abecedario=abc, lista_abc=listado, lista_pal=palabraL)

    if request.method=='POST':
        existe=False
        valor=request.form['valor']
        for dic in palabraL:
            if valor in dic: 
                dic[valor]=valor
                existe=True
                image=f"/static/images/monito-{conteo}.png"
        if not existe:
            conteo+=1 
            image=f"/static/images/monito-{conteo}.png"

        if conteo>6:
            conteo=0
            palabra=random.choice(palabras)
            palabraL=palabra_toList(palabra)
            image=f"/static/images/monito-{conteo}.png"
            letras=[{'letra':x, 'id_letra':x}for x in abc]
            listado=[(d['letra'],d['id_letra']) for d in letras]
            
        
        return render_template('index.html', imagen=image, abecedario=abc, lista_abc=listado, lista_pal=palabraL)
        

    
if __name__=='__main__':
    app.run(debug=True)
