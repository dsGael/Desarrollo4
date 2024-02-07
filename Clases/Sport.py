''' class Sport '''
class Sport:
    def __init__(self,name:str,num_players:int,league:str):
        self.name = name
        if type(num_players)!= int:
            num_players=int(num_players)
        self.num_players = num_players
        self.league = league
    
    def __str__(self):
        return_string = f"Sport:{self.name} Num.Players:{self.num_players} League:{self.league}"
                        
        return return_string
    
    def __repr__(self) -> str:
        return_string = f"""Sport(name:'{self.name}',num_players='{self.num_players}',
                            league='{self.league}')
                        """
        return return_string
    
if __name__ == "__main__":
    s = Sport("Soccer",11,"LMX")
    print(s)
    b = Sport("Beisbol",9,"LMP")
    print(b)
    print(repr(b))