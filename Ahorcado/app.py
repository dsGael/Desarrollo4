from flask import Flask, render_template,request
from os import path
from funciones import lee_archivo, palabra_toList, ganador
import random


app=Flask(__name__)
conteo=0
palabras=lee_archivo("Ahorcado/palabras.txt") 
abc="abcdefghijklmnopqrstuvwxyz"
letras=[x for x in abc]

@app.route('/', methods=['GET','POST'])
def index():
    global conteo
    global palabraList
    global listado
    global palabra
    
    global chequeo
     
    if request.method=='GET':
        palabra=random.choice(palabras)
        palabraList=palabra_toList(palabra)
        image=f"/static/images/monito-{conteo}.png"
        Lista_letras=[{'letra':x, 'id_letra':x}for x in abc]
        listado=[(d['letra'],d['id_letra']) for d in Lista_letras]
        return render_template('index.html', imagen=image, abecedario=abc, lista_abc=listado, lista_pal=palabraList)
   
    if request.method=='POST':
        chequeo=False
        existe=False
        valor=request.form['valor']
        for dic in palabraList:
            if valor in dic: 
                dic[valor]=valor
                existe=True
                chequeo=ganador(palabraList)
                image=f"/static/images/monito-{conteo}.png"
               
                    
                    
        if not existe:
            conteo+=1 
            image=f"/static/images/monito-{conteo}.png"
            
           
      
        
        return render_template('index.html', imagen=image, abecedario=abc, lista_abc=listado, lista_pal=palabraList ,conteo=conteo,chequeo=chequeo)
        

    
if __name__=='__main__':
    app.run(debug=True)
