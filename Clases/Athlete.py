class Athlete:
    def __init__(self, name) -> None:
        self.name = name

    def display(self) -> None:
        print(f"Name:{self.name}")

    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"Athlete(name='{self.name}')"
    
if __name__ == "__main__":
    a = Athlete("Ana G.")

    a.display()
    print(a)
    print(repr(a))
    b = eval(repr(a))
    print(b)
    print(f"a:{type(a)},b:{type(b)}")
    print(f"a:{id(a)} b:{id(b)}")