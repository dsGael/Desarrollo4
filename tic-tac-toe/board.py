from colorama import Fore,Back,Style,Cursor

def display_tablero(tablero:dict):
    reset= Style.RESET_ALL
    bg=Back.BLACK
    blue=Fore.BLUE
    board_color = Fore.LIGHTCYAN_EX
    x_color =Fore.RED
    o_color=Fore.LIGHTGREEN_EX
    X= x_color+"X"
    O = o_color+"O"
    BD=board_color+" ------------- "
    BS=board_color+" | "
    d={}
    for k,v in tablero.items():
        if v=="X":
            d[k] = X + BS
        elif v == "O":
            d[k]=O + BS
        else:
            d[k]= blue + str(k) + BS
    Cursor.POS(10,5)
  
    
    
    print(Cursor.POS(20,5)+f"{bg}{BS}{d[0]}{d[1]}{d[2]}{reset}")
    print(Cursor.POS(20,6)+f"{bg}{BD}{reset}")
    print(Cursor.POS(20,7)+f"{bg}{BS}{d[3]}{d[4]}{d[5]}{reset}")
    print(Cursor.POS(20,8)+f"{bg}{BD}{reset}")
    print(Cursor.POS(20,9)+f"{bg}{BS}{d[6]}{d[7]}{d[8]}{reset}")
    print(Style.RESET_ALL)

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
    print(Cursor.POS(1,18)+f"<<Jugador:{s['Jugador']}>> <<IA:{s['IA']}>> <<Empates:{s['Empates']}>>")

def play_again():
    continuar=True
    print(Cursor.POS(1,20)+"¿Otra partida? \n1 >> Si \n 2 >> No"")
    
    opcion=input()
    if opcion!="1":
        continuar=False
        print(Cursor.POS(1,22)+"bai bai")
    return continuar

def juega_usuario(tab):
    turno_correcto=False
    usuario= input(Cursor.POS(1,12)+"Escoja celda:\n")
    usuario=int(usuario)
    if usuario in tab:
        if tab[usuario]== str(usuario):
            tab[usuario]="X"
            turno_correcto=True
        else:
            print(Cursor.POS(1,14)+f"Casilla {usuario} Ocupada \nElija otra opción\n")
    return turno_correcto
