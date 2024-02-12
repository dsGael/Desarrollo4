import colorama
from colorama import Fore, Back, Style


class tablero:
    def __init__(self, color_fondo,color_rayas,color_numeros, colorX,colorO)-> None:
        self.lista_num=[x for x in range(0,9)]
        self.dicc_pos={x:str(x) for x in self.lista_num}
        self.pos_ganadoras=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.color={"rayas":color_rayas,"simbolos":color_simbolos,"fondo":color_fondo, "numeros":color_numeros,"X":colorX,"O":colorO}
        

    def display_tablero(self):
        tablero=self.dicc_pos
        reset= Style.RESET_ALL
        bg=self.color["fondo"]
        blue=self.color["numeros"]
        board_color =self.color["rayas"]
        x_color =self.color["X"]
        o_color=self.color["O"]
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
