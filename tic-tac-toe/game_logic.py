'''
logica del programa del gato
'''
tablero=[x for x in range(0,9)]
tab_dict={x:str(x) for x in range(0,9)}

def display_tablero(tab:dict):
    print(f"{tab[0]} | {tab[1]} | {tab[2]}")
    print("--+---+---")
    print(f"{tab[3]} | {tab[4]} | {tab[5]}")
    print("--+---+---")
    print(f"{tab[6]} | {tab[7]} | {tab[8]}")        

print(f"tablero: {tablero}")
print(f"tab_dict: {tab_dict}")


def game(tab:dict):
    while True:
        display_tablero(tab)
        celda= input("Selecciona una celda: ")
        if celda in tab:
            

game(tab_dict)