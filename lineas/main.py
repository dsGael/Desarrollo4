import linea.linea as linea 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    X=[x for x in range (0,10)]
    m=2
    b=3
    Y=linea.calcula_y(X,m,b)
    plt.plot(X,Y)
    plt.show()

    
