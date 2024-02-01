from Atleta import Athelete
from Sport import Sport

class Team:
    def __init__(self, name:str, sport:Sport) -> None:
        self.name = name
        self.sport = sport
        self.players = []

    def add_player(self, player:Athelete) -> None:
        self.players.append(player.name)

    def display(self):
        print(f"Team: {self.name}")
        print(f"Sport: {self.sport.name}")
        print(f"League: {self.sport.league}")
        print("The team members are:")
        for athlete in self.players:
            print(athlete)

if __name__ == "__main__":
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Lakers", s)
    aaron = Athelete('Aaron', 15, 'basketball', 'Lakers')
    julian = Athelete("Julian", 16, "basketball", "Lakers")
    emilio = Athelete("Emilio", 17, "basketball", "Lakers")
    lakers.add_player(aaron)
    lakers.add_player(julian)
    lakers.add_player(emilio)
    lakers.display()