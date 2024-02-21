
class Revista:
    def __init__(self,titulo:str,catalogo:str):
        self.titulo=titulo
        self.catalogos=set()
        self.catalogos.add(catalogo)

    def __str__(self) -> str:
        return f"{self.titulo}-{self.catalogos}"
    
    

if __name__ == '__main__':
    revista=Revista("papu","catalogo")
    print(revista.titulo)
    