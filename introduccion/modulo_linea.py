

def linea(x,m,b):
    x=[1,2,3]
    m=1.5
    b=2.0
    return m*x+b

if __name__=="__main__":
    X=[x for x in range (0,10)]
    Y=[linea(x,1.5,2) for x in range (0,10)]
    coord= zip(X,Y)

