from Team import Team
import random
class Game:
    def __init__(self,A:Team,B:Team) -> None:
        self.A=A
        self.B=B
        self.score=dict()
        self.score[A.name]=0
        self.score[B.name]=0

        def play(self):
            sports_list=["Baseball","Soccer","Basketball","NFL"]
            sports_dict={"Baseball": [x for x in range(0,10)],  "Basketball": [x for x in range(90,120)], "NFL": [x for x in range(0,57,7)], "Soccer": [x for x in range(0,6)]}
                         
            for s in sports_list:
                if self.A.sport.name == s and self.B.sport.name == s:
                    self.score[A.name ]= random.choice(sports_dict[s])
                    self.score[B.name ]= random.choice(sports_dict[s])

        def __str__(self) -> str:
            return f"{self.A.name}:{self.score[self.A.name]} - {self.score[self.B.name]}:{self.B.name}"