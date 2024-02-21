'''
Calcula datos estadisticos de una lista, usando argumentos
'''
import argparse
import calcula

def main(args, choices:list)->None:
    operacion=args.op
    listado=args.enteros
    for c in choices:# WIP
        dict={c:"print(f'{c.capitalize()}: {calcula."+c+"(listado)}')"}
        
    adict={"suma":"print(f'Suma: {calcula.suma(listado)}')",
        "promedio":"print(f'Promedio: {calcula.promedio(listado)}')",
        "moda":"print(f'Moda: {calcula.moda(listado)}')",
        "todas":"no implementado"}
        # "todas":"print(f'Suma: {calcula.suma(listado)}')\n print(f'Promedio: {calcula.promedio(listado)}')\nprint(f'Moda: {calcula.moda(listado)}')"}
    eval(dict[operacion]) 
    

if __name__=="__main__":
    choices=["suma","promedio","moda","todas"]
    parser=argparse.ArgumentParser(description="Calcula datos estadisticos de una lista")
    parser.add_argument("enteros", metavar="N", type=int, nargs="+", help="Lista de flotantes")
    parser.add_argument("--operacion","-o", type=str, dest="op", choices=choices)
    args=parser.parse_args()
    for c in choices:
        dict={c:"print(f'{c.capitalize()}: {calcula."+c+"(listado)}')"}
        print(dict)
    main(args, choices)
