from Athlete import Athlete
from Sport import Sport
from Team import Team
import random

class Game:
    def __init__(self, A:Team, B:Team) -> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        sports_list = ['Baseball', 'Basketball','NFL','Soccer']
        sports_dict = { 'Baseball':   [x for x in range(0,10)],
                        'Basketball':[x for x in range(90,120)],
                        'NFL':        [x for x in range(0,57,7)],
                        'Soccer':     [x for x in range(0,6)]
                        }
        for s in sports_dict.values():
            if self.A.sport.name == s and self.B.sport.name == s:
                self.score[self.A.sport.name] = random.choice( sports_dict[s] )
                self.score[self.B.sport.name] = random.choice( sports_dict[s] )

    def __str__(self):
        return f"{self.A.name}:{self.score[self.A.name]} - {self.score[self.B.name]}:{self.B.name}"
    
    
if __name__ == "__main__":
    dt = ['Jordan','Jhonson','Pipen','Bird','Kobe']
    cz = ['Bjovik','Czack','Pfeizer','Leonard','Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basket = Sport("Basketball",5,"DreamTeam")
    t = Team("Dream Team",basket)
    c = Team("Czeck Republic",basket)
    for a in players_a:
        t.add_player(a)
    for b in players_b:
        c.add_player(b)
    game = Game(t,c) 
    game.play()
    print(game)
            
    

    