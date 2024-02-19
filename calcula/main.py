'''
Calcula datos estadisticos de una lista, usando argumentos
'''
import argparse
import calcula

def main(listado:list)->None:
    print(f"Suma: {calcula.suma(listado)}")
    print(f"Promedio: {calcula.promedio(listado)}")
    print(f"Moda: {calcula.moda(listado)}")

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Calcula datos estadisticos de una lista")
    parser.add_argument("enteros", metavar="N", type=int, nargs="+", help="Lista de flotantes")
    args=parser.parse_args()
    print(args.enteros)
    main(args.enteros)
