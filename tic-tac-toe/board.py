from colorama import Fore,Back,Style,Cursor

def display_tablero(tablero:dict):
    reset= Style.RESET_ALL
    bg=Back.WHITE
    blue=Fore.BLUE
    board_color = Fore.LIGHTCYAN_EX
    x_color =Fore.RED
    o_color=Fore.GREEN
    X= x_color+"X"
    O = o_color+"O"
    BD=board_color+"----------"
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
    print(f"{bg}{BD}{reset}")
    print(f"{bg}|{d[0]}{d[1]}{d[2]}{reset}")
    print(f"{bg}{BD}{reset}")
    print(f"{bg}|{d[3]}{d[4]}{d[5]}{reset}")
    print(f"{bg}{BD}{reset}")
    print(f"{bg}|{d[6]}{d[7]}{d[8]}{reset}")
    print(Style.RESET_ALL)
