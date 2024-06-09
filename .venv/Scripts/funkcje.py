import math
import matplotlib.pyplot as plt
from scipy.stats import chi2
import numpy as np
from scipy.stats import kstest

#------------------------funkcje--------------------------
def nwd(a_nwd, b_nwd):
    while b_nwd != 0:
        a_nwd, b_nwd = b_nwd, a_nwd % b_nwd
    return a_nwd

def dobor_a(m_pom, a_candidate):
    if (nwd(a_candidate, m_pom) == 1) and ((a_candidate - 1) % 4 == 0):
        print("a jest okej")
    else:
        print("a nie jest okej")

def dobor_c(m,c):
    if nwd(m, c) == 1:
        print("c jest okej")
    else:
        print("c nie jest okej")

def LCG(seed, a, c, m, zakres):
    x = [seed]
    for _ in range(zakres):
        x.append(((a * x[-1] + c) % m))
    return x  # Zwracamy całą listę, w tym ziarno

def middle_square(seed, zakres):
    x = [seed]
    for i in range(1, zakres):
        kwadrat = str(x[i-1] ** 2).zfill(8)
        x.append(int(kwadrat[len(kwadrat) // 4:3 * len(kwadrat) // 4]))
    return x

def slaby_generator(seed, zakres):
    # seed = 1
    x = [seed]
    for i in range(1, zakres):
        x.append(((x[i-1]*5) + 1)%16)
    return x

def generator_bardzo_pseudolosowy(zakres, przyrost):
    x = []
    aktualna_liczba = 0.0

    for _ in range(zakres):
        x.append(aktualna_liczba)
        aktualna_liczba += przyrost

    return x

def wybierz_losowe(losowe, druga_lista, ile_wybrac):
    if len(losowe) != len(druga_lista):
        raise ValueError("Listy muszą mieć tę samą długość")

    ile_wybrac = min(ile_wybrac, len(losowe))

    indeksy_wartosci = list(enumerate(losowe))

    indeksy_wartosci.sort(key=lambda x: x[1])

    wybrane_indeksy = [indeks for indeks, _ in indeksy_wartosci[:ile_wybrac]]

    x = [druga_lista[indeks] for indeks in wybrane_indeksy]

    return x

def konwersja_do_01(liczby, m):
    liczby_01 = [liczba / m for liczba in liczby]
    return liczby_01

def dystrybuanta(liczby, zakres):
    liczby_pom = np.sort(np.array(liczby))
    x = np.linspace(0, zakres, num=1000)
    y = np.searchsorted(liczby_pom, x, side='right') / len(liczby_pom)

    plt.plot(x, y, drawstyle='steps-post')
    plt.xlabel('Wartość')
    plt.ylabel('Fn(x)')
    plt.title('Wykres dystrybuanty')
    plt.grid()
    plt.show()