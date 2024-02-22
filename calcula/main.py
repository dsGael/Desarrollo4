'''
Calcula datos estadisticos de una lista, usando argumentos
'''
import argparse
import calcula

def main(args)->None:
    operacion=args.o
    listado=args.enteros
    choices=["suma","promedio","moda","todas"]
    dict={"suma":"","promedio":"","moda":"","todas":""}
    for c in choices:# WIP
        if c == "todas":
            dict[c]="print('no implementado')"
        else:
            dict[c]="print(calcula."+c+"(listado))"
        
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
    parser.add_argument("--operacion","-o", type=str, dest="o", choices=choices)
    args=parser.parse_args()
    main(args)
