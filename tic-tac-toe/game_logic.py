import random 
'''
logica del programa del gato
'''
def reset_tablero():
    tablero=[x for x in range(0,9)]
    tab_dict={x:str(x) for x in range(0,9)}
    return tab_dict


def display_tablero(tab:dict):
    print(f"{tab[0]} | {tab[1]} | {tab[2]}")
    print("--+---+---")
    print(f"{tab[3]} | {tab[4]} | {tab[5]}")
    print("--+---+---")
    print(f"{tab[6]} | {tab[7]} | {tab[8]}")        


def IA(board:dict):
    ocuppied = True
    while ocuppied==True:
        r=random.choice(list(board.keys()))
        if board[r] == str(r):
            ocuppied=False
            board[r]="O"


def juega_usuario(tab):
    turno_correcto=False
    usuario= input("Escoja celda:\n")
    usuario=int(usuario)
    if usuario in tab:
        if tab[usuario]== str(usuario):
            tab[usuario]="X"
            turno_correcto=True
        else:
            print(f"Casilla {usuario} Ocupada \nElija otra opción\n")
    return turno_correcto



def game(tab:dict):
    turnos=0
    diccionario={'ganador':''}
    
    while turnos <8:
        display_tablero(tab)
        correcto=juega_usuario(tab)
        if correcto:
            turnos+=1
            gana=win(tab)
        
            if gana:
                diccionario["ganador"]="Jugador :)"
                display_tablero(tab)
                print("Ganaste!")
                
                break
            IA(tab)  
            gana=win(tab)
        

            if gana:
                diccionario["ganador"]="IA :("
                display_tablero(tab)
                print("Gana IA")
                
                break
                
            
            turnos+=1          
    display_tablero(tab)
    return diccionario
        

def win(tab):

    lista_lineas=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for comb in lista_lineas:
        if tab[comb[0]]==tab[comb[1]]==tab[comb[2]]:
            return True
    return False


def game_cycle(tab):
    

    d=game(tab)
    if d['ganador']!="":
        print(f"Ganador: {d['ganador']}")
        if d['ganador']=="Jugador :)":
            score['Jugador']+=1
        elif d['ganador']=="IA :(":
            score['IA']+=1
        
    else:
        print("Empate")
        score['Empates']+=1
    print(f"Marcador: {score}")
        

if __name__ == "__main__":
    opcion=1
    continuar=True
    score={"Jugador":0,"IA":0, "Empates":0}
    while continuar:
        tab=reset_tablero()
        print("TIC TAC TOE")
        game_cycle(tab)
        print("¿Otra partida?")
        print("1 >> Si")
        print("2 >> No")
        opcion=input()
        if opcion!="1":
            continuar=False
            print("bai bai")
            
