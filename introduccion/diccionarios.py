ingenieria={}
ingenieria['ISI']='Ingenieria de Sistemas de Informacion'
ingenieria['IIS']='Ingenieria Industrial y de Sistemas'
ingenieria['IME']='Ingenieria Mecatrónica'
print(ingenieria)

minas=dict()
minas['IM']='Ingenieria de Minas'
minas['IME']='Ingenieria Mecanica de Suelos'
minas['IMM']='Ingenieria de Minas y Metalurgia'
print(minas)

facultad={'Ingenieria':ingenieria,'Minas':minas}
print(facultad['Ingenieria']['ISI'])
print(facultad['Minas']['IMM'])
print("\n----------------------")
if 'civil' in facultad:
    print(facultad['civil'])
else:
    print('No existe la carrera de civil')

try:
    print(facultad['civil'])
except KeyError:                    
    print('No existe la carrera de civil')    

    
facultad['civil']={}
facultad['civil']['IC']='Ingenieria Civil'

if 'civil' in facultad:
    print(facultad['civil'])

print("\n----------------------")

cadena="el caballo corre por el campo"
diccionario={}
for letra in cadena:
    if letra in diccionario:
        diccionario[letra]+=1
    else:
        diccionario[letra]=1

print(diccionario)

for k,v in diccionario.items():
    print(k,v)

print("\n----------------------")
diccionario_ordenado= sorted(diccionario.items(),key=lambda item: item[1],reverse=True)
diccionario_ordenado=dict(diccionario_ordenado)
print(diccionario_ordenado)

for k,v in diccionario_ordenado.items():
    print(f"K:{k} V: {v}")


diccionario_ordenado= dict(sorted(diccionario.items(),key=lambda item: item[0],reverse=False))

for k,v in diccionario_ordenado.items():
    print(f"K:{k}  \tV: {v}")


    
