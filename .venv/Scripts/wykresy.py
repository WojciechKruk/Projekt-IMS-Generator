import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def wykres_liczb(liczby):
    plt.plot(liczby)
    plt.title('Wykres kolejnych wygenerowanych liczb')

    plt.xlabel('Indeks')
    plt.ylabel('Wartość x')
    plt.show()

def wykres_punktow(liczby):
    #wykres (x1,x2)

    if len(liczby) % 2 != 0:
        liczby.pop()

    x = liczby[::2]
    y = liczby[1::2]

    plt.plot(x, y, color='blue', linestyle='-', marker='o', markerfacecolor='red', markeredgecolor='red', markersize=8)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def wykres_punktow_przesuniecie(liczby, przesuniecie):
    x = []
    y = []

    for i in range(len(liczby) - przesuniecie):
        x.append(liczby[i])
        y.append(liczby[i + przesuniecie])

    plt.plot(x, y, color='blue', linestyle='-', marker='o', markerfacecolor='red', markeredgecolor='red', markersize=8)

    plt.title(przesuniecie)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def wykres_punktow_3d(liczby):
    if len(liczby) % 3 != 0:
        liczby.pop()
        if len(liczby) % 3 != 0:
            liczby.pop()

    x = liczby[::3]
    y = liczby[1::3]
    z = liczby[2::3]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='blue')
    ax.scatter(x, y, z, color='red')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('')
    plt.show()