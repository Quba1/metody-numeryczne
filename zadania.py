import numpy as np
import matplotlib.pyplot as plt
'''
Zadania
    1. Poniżej funkcji main() dodaj funkcję f1(x), która będzie obliczać wartość -x/10

    2. Poniżej deklaracji tablic arr_x i arr_y napisz kod wyliczający całkę f1(x) 
        przy użyciu omówionej metody różnic skończonych

    3. Dodaj do funkcji main() drugą deklarację tablic x & y i kod wyliczający
        bardzo dokładną wartość całki f1(x) (możesz skopiować część istniejącego kodu)

    4. Dodaj funkcję f2(x) według własnego pomysłu (np. taką, której całki nie potrafisz
        policzyć) i oblicz jej całkę w funkcji main()

    5. Dodaj funkcję f3(y) i użyj jej w funkcji main() tak aby zasymulować chłodzenie
        ciała zgodnie z prawem stygnięcia Newtona 
    
    6. Dodaj funkcję f4(x, y) reprezentującą paraboloidę hiperboliczną, użyj jej w main()
        i przenanalizuj stabilność metody Eulera dla tej metody

    7. Zaimplementuj metodę Heuna i porównaj jej dokładność i stabilność do metody Eulera

    Zadanie dodatkowe: Zaimplementuj metodę Runge-Kutta 4-tego rzędu i przeanalizuj jej stabilnosć
'''


def main():

    delta_x = 1
    initial_value = 6
    x_max = 10

    # compute approximated function
    arr_x = np.arange(0, x_max, step=delta_x)
    arr_y = np.zeros(arr_x.shape)

    # plot results
    plt.plot(arr_x, arr_y, "g")
    plt.show()


if __name__ == "__main__":
    main()
