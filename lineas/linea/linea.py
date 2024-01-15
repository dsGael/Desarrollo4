
def linea(x, m, b):
    
    return (m * x) + b

def calcula_y(X,m,b):
    Y = [linea(x, m, b) for x in X]
    return Y

if __name__ == "__main__":
    X = [x for x in range(10)]
    m = 1.5
    b = 2
    Y=calcula_y(X,m,b)
    print(X,Y)
   
