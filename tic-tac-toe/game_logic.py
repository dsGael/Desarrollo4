import random 
import board


'''
logica del programa del gato
'''
def reset_tablero():
    tablero=[x for x in range(0,9)]
    tab_dict={x:str(x) for x in range(0,9)}
    return tab_dict


#def display_tablero(tab:dict):
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
        board.display_tablero(tab)
        correcto=juega_usuario(tab)
        if correcto:
            turnos+=1
            gana=win(tab)
            if gana:
                diccionario["ganador"]="Jugador"
                board.display_tablero(tab)
                print("Ganaste!")
                break
            IA(tab)  
            gana=win(tab)
            if gana:
                diccionario["ganador"]="IA"
                board.display_tablero(tab)
                print("Gana IA")
                break              
            turnos+=1          
    board.display_tablero(tab)
    return diccionario
        

def win(tab):
    lista_lineas=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for comb in lista_lineas:
        if tab[comb[0]]==tab[comb[1]]==tab[comb[2]]:
            return True
    return False


def game_cycle():
    opcion=1
    continuar=True
    score={"Jugador":0,"IA":0, "Empates":0}
    while continuar:
        tab=reset_tablero()
        #print("TIC TAC TOE\n")
        d=game(tab)
        display_score(score,d)
        continuar = play_again()
   
        
def display_score(s:dict,d:dict):
    '''
    s= diccionario de scores keys
    d= diccionario cobn el ganador del juego anterior key
    '''
    if d['ganador']!="":
        print(f"Ganó: {d['ganador']}")
        s[d['ganador']]+=1   
    else:
        print("¡Empate!")
        s['Empates']+=1
    print(f"<<Jugador:{s['Jugador']}>> <<IA:{s['IA']}>> <<Empates:{s['Empates']}>>")


def play_again():
    continuar=True
    print("¿Otra partida?")
    print("1 >> Si")
    print("2 >> No")
    opcion=input()
    if opcion!="1":
        continuar=False
        print("bai bai")
    return continuar

if __name__ == "__main__":
   game_cycle()
    
        
        
                
