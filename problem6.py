import control
from control.matlab import *
import matplotlib.pyplot as plt

def main():
    s = TransferFunction.s
    
    #TF with gain 1, 3, 5
    gain = [1,2,5]
    TF = ((s**2) - (2*s) + (4))/((s**2)  + (4*s) + (2))


    a, b = control.root_locus(TF, kvect=gain, plot=True, xlim=[-5,5], ylim=[-5,5])
    plt.show()
    print(a)
    print(b)
    
    
    
if __name__ == '__main__':
    main()