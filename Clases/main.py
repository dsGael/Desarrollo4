from Atleta import Athelete
from Sport import Sport
from Team import Team

def main():
    players = ["Aaron", "Julian", "Emilio", "Jorge", "Luis", "Ricardo", "Carlos", "Javier", "Miguel", "Jose"]

    players_objects = [Athelete(x) for x in players]
    s = Sport("Soccor", 11, "DreamTeam")
    t = Team("DreamTeam", s)
    for player in players_objects:
        t.add_player(player)
    t.display()

main()