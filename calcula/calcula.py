

def suma(list:list)->float:
    return sum(list)

def promedio(list:list)->float:
    return sum(list)/len(list)

def main(lista:list)->None:
    print(f"Suma: {suma(lista)}")
    print(f"Promedio: {promedio(lista)}")

def moda(list:list)->float:
    dic={x:0 for x in list}
    for x in list:
        dic[x]+=1
       
    maximo=max(dic.values())
    for x in dic:
        if dic[x]==maximo:
            maximo=x
    return maximo

if __name__=="__main__":
    lista=[x for x in range(1,10)]
    main(lista)