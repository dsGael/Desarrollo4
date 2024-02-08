from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json

def main0():
    players = ['Chicharito','Piojo','Alexis Vega',
               'La Tota','Chuki','Tecatito',
               'Cuahutemoc','Hermoso','Piqué',
               'Messi','Ochoa'
               ]
    players_objects = [Athlete(x) for x in players]
    s = Sport("Soccer",11,"FIFA")
    t = Team("Dream Team",s)
    for a in players_objects:
        t.add_player(a)
    #t.display()
    players_b = ['Iniesta','Xavi','Neymar','Hulk','Lewandoski','Puyol',
                 'Miguel','Aarón','Francisco','Maradona','Kaká']
    players_objects2 = [Athlete(x) for x in players_b]
    s2 = Sport("Soccer",11,"FIFA")
    t2 = Team("Equipo Ensueño",s2)
    for a in players_objects2:
        t2.add_player(a)

    torneo = { t.name:t.to_json(), t2.name:t2.to_json()}
    print(torneo)
    #torneo_json = json.dumps(torneo)
    
    with open("torneo_soccer.json","w", encoding="utf8") as archivo:
        archivo.write(str(torneo))

def procesa_diccionario(diccionario:dict) -> dict:
    diccionario_equipos = {}
    for k1,v1 in diccionario.items():
        for k2,v2 in v1.items():
            if(k2=="players"):
                lista_atleta=[Athlete(x) for x in v2]
             
            if(k2=="sport"):
                s=Sport(v2['name'],v2['num_players'],v2['league'])
                
            if(k2=="name"):
                nombre_eq=v2
                

        equipo=Team(nombre_eq,s)
        for a in lista_atleta:
            equipo.add_player(a)
        diccionario_equipos[k1]=equipo
    return diccionario_equipos


def main():
    with open("torneo_soccer.json","r", encoding="utf8") as archivo:
      json_leido=json.load(archivo)
    equipos=procesa_diccionario(json_leido)
    for equipo in equipos.items():
        print(equipo)
        print()


if __name__ == "__main__":
    main()



