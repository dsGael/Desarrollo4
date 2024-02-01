class Sport:
    def __init__(self, name:str, num_players:int, league:str):
        self.name = name
        self.num_players = num_players
        if self.num_players != int:
            self.num_players = int(num_players)
        self.league = league
        

    def __str__(self):
        return_string = f'''Sport: {self.name}
                            Num.Players: {self.num_players} 
                            League: {self.league} 
                        '''
        return return_string
    
    def __repr__(self) -> str:
        return_string = f'''Sport(name:'{self.name}'
                            Num.Players = '{self.num_players}'
                            League = '{self.league}')
                        '''
        return return_string

if __name__ == "__main__":
    s = Sport("Basketball", 5, "NBA")
    print(s)
    b = Sport("Baseball", 9, "MLB")
    print(b)
    print(repr(s))