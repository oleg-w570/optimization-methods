import numpy as np
import matplotlib.pyplot as plt
import pandas


x = np.linspace(-5, 5, 1000)
y = np.abs(x - 1)

plt.plot(x, y)


def dichotomy(Q, a: float, b: float, delta: float):
    c = 0.5 * (a + b)
    Q_c = Q(c)

    while b - a > delta:
        x = 0.5 * (a + c)
        Q_x = Q(x)
        y = 0.5 * (c + b)
        Q_y = Q(y)

        if Q_x <= Q_c < Q_y:
            b = c
            c = x
            Q_c = Q_x
        elif Q_x > Q_c <= Q_y:
            a = x
            b = y
        else:
            a = c
            c = y
            Q_c = Q_y

    return a, b


a, b = dichotomy(lambda x: abs(x - 1), -5, 5, 0.01)
print(a, b)
plt.grid()
plt.show()
