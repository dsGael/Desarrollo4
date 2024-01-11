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

    

