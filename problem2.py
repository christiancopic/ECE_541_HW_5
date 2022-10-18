import control
from control.matlab import *
import matplotlib.pyplot as plt

def main():
    s = TransferFunction.s
    # A = (wn ^ 2)/(s^2 + 2*zeta*wn*s + wn^2)
    # 1) wn = 2 zeta = 0
    A1 = ((2)**2)/((s**2)  + (2*0*s) + (2**2))
    # 2) wn = 2 zeta = 0.1
    A2 = ((2)**2)/((s**2)  + (2*0.1*s) + (2**2))
    # 3) wn = 1 zeta = 0
    A3 = ((1)**2)/((s**2)  + (2*0*s) + (1**2))
    # 4) wn = 1 zeta = 0.2
    A4 = ((1)**2)/((s**2)  + (2*0.2*s) + (1**2))

    T1, Yout1 = control.impulse_response(A1)
    T2, Yout2 = control.impulse_response(A2)
    T3, Yout3 = control.impulse_response(A3)
    T4, Yout4 = control.impulse_response(A4)

    plt.subplot(2,2,1)
    plt.plot(T1, Yout1)
    plt.title("1st case")

    plt.subplot(2,2,2)
    plt.plot(T2, Yout2)
    plt.title("2nd case")

    plt.subplot(2,2,3)
    plt.plot(T3, Yout3)
    plt.title("3rd case")

    plt.subplot(2,2,4)
    plt.plot(T4, Yout4)
    plt.title("4th case")

    plt.suptitle("Question 2: CP5.3")

    plt.show()
    


if __name__ == '__main__':
    main()