# Gael Humberto Borchardt Castellanos 05/04/2024

class Revista:
    def __init__(self, titulo:str,catalogo:str, sjr:str,q:str,h_index:str,total_citas:str) :
         self.titulo=titulo
         self.catalogo=set()
         self.catalogo.add(catalogo)
         self.sjr=float(sjr)
         self.q=q
         self.h_index=int(h_index)
         self.total_citas=int(total_citas)
    
    def __repr__(self):
        return f'{self.titulo} |{self.catalogo} |{self.sjr}| {self.q} |{self.h_index} |{self.total_citas}'

    def __str__(self):
        return f'{self.titulo} |{self.catalogo} |{self.sjr}| {self.q} |{self.h_index} |{self.total_citas}'
        

def main():
    revista=Revista('hola','catalogo',1.2,'Q1',150,10)
    revista2=Revista('hola','catalogo',1.6,'Q2',140,10)

    print(revista)
    print(revista2)

if __name__=='__main__':
    main()