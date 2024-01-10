lunas=["lunas","phobos","io","titan"]
moons=lunas
print(f"lunas: {lunas}")
print(f"moons: {moons}")

moons.append("europa")
lunas.append("galymede")


print(f"lunas id: {id(lunas)}{lunas}")
print(f"moons id: {id(moons)}{moons}")

moons=lunas.copy()
print(" \n copy")
moons.append("12545")
print(f"lunas id: {id(lunas[4])}{lunas}")
print(f"moons id: {id(moons)}{moons}")

moons.insert(0,"lunasAAAa")


planetas_sw=["Hoth", "Tatooine","Naboo","Mustafar","Endor","Kamino"]
planetas_sw.sort()
print(planetas_sw )
print(" \n")
moons_sw=["yavin 4","dagobah", "couruscant","kashyyyk","geonosis","utapau"]

lista_lunas=[lunas,moons_sw]
print(lista_lunas )
print(" \n")
print(lista_lunas[1][5])

print(lunas.index("titan"))



for i,planetas_sw in enumerate(planetas_sw):
    print(i,planetas_sw)


A=[]
B=[]
for i in range(0,10):
    A.append(i)
    if i%2==0:
        B.append(i)

print(A)  
print(B)
