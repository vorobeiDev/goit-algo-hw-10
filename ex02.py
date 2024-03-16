import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2

def draw():
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


def monte_carlo_integration(f, a, b, n=10000):
    x = np.random.uniform(a, b, n)
    y = f(x)
    integral = (b - a) * np.mean(y)
    return integral


if __name__ == '__main__':
    a = 0
    b = 2

    draw()
    result, error = spi.quad(f, a, b)
    result_mc = monte_carlo_integration(f, a, b)

    print("Інтеграл вирішений з quad: ", result)
    print("Інтеграл вирішений симуляцією : ", result_mc)
