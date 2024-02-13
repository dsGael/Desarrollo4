
from colorama import Fore, Back, Style,Cursor
from jugador import Jugador

class tablero:
    def __init__(self, color_fondo=Back.WHITE,color_rayas=Fore.LIGHTCYAN_EX,color_numeros=Fore.BLUE, colorX=Fore.RED,colorO=Fore.GREEN)-> None:
        self.lista_num=[x for x in range(0,9)]
        self.dicc_pos={x:str(x) for x in self.lista_num}
        self.pos_ganadoras=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.color={"rayas":color_rayas,"fondo":color_fondo, "numeros":color_numeros,"X":colorX,"O":colorO}
        
    def Checa_win(self):
        tab=self.dicc_pos
        for comb in self.pos_ganadoras:
            if tab[comb[0]]==tab[comb[1]]==tab[comb[2]]:
                return True
        return False

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

    def juega_usuario(self, jugador:Jugador):
        turno_correcto=False
        tab=self.dicc_pos
        usuario= input(Cursor.POS(1,12)+"Escoja celda:\n")
        usuario=int(usuario)
        if usuario in tab:
            if tab[usuario]== str(usuario):
                tab[usuario]=jugador.simbolo
                turno_correcto=True
            else:
                print(Cursor.POS(1,14)+f"Casilla {usuario} Ocupada \nElija otra opción\n")
        return turno_correcto

    def reset_tablero(self):
        self.dicc_pos={x:str(x) for x in self.lista_num}


if __name__ == "__main__":
    t=tablero()
    simbolos=['X','O']
    j=Jugador("gael","X",simbolos)
    t.display_tablero()
    t.juega_usuario(j)
    t.juega_usuario(j)
    t.juega_usuario(j)
    if t.Checa_win():
        print(Cursor.POS(1,4)+f"Gana: {j.nombre}")
    t.display_tablero()
    