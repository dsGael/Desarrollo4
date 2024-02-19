from jugador import Jugador
from tablero import tablero
import os

class Juego:
    def __init__(self,tablero:tablero,jugador1:Jugador,jugador2:Jugador)-> None:
        self.tablero=tablero
        self.jugador1=jugador1
        self.jugador2=jugador2
        self.turnos=0

    def playing(self,moviendo:Jugador,espera:Jugador)->bool:
            mov=False
            ganador=False
            while mov==False:
                print(f"Turno de {moviendo.nombre}")
                mov= self.tablero.juega_usuario(moviendo)        
            self.turnos+=1
            self.tablero.display_tablero()

            if self.tablero.Checa_win():
                print(f"Ganador: {moviendo.nombre}")
                moviendo.juegos['ganados']+=1
                espera.juegos['perdidos']+=1
                ganador= True
            return ganador

    def inicia_juego(self):
        self.tablero.reset_tablero()
        
        while self.turnos<9:
            self.tablero.display_tablero()
            ganador=self.playing(moviendo=self.jugador1,espera=self.jugador2)
            if ganador!=True: 
                ganador= self.playing(moviendo=self.jugador2,espera=self.jugador1)
                if ganador:                    
                    break
            


if __name__ =="__main__":
    simbolos=['X','O']
    j1=Jugador('Juan','X',simbolos)
    j2=Jugador('Ana','O',simbolos)
    t=tablero()
    juego=Juego(t,j1,j2)
    juego.inicia_juego()
                

                    

