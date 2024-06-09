import math
import matplotlib.pyplot as plt
from scipy.stats import chi2
import numpy as np
from scipy.stats import kstest
from funkcje import *
from wykresy import *
from testy import *

def konwersja_do_01(liczby, m):
    liczby_01 = [liczba / m for liczba in liczby]
    return liczby_01

# ------------generator-z-wykladu--------------------

class LinearCongruentialGenerator:

    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.state = seed
        self.k = len(a)

    def next(self):
        next_value = sum(self.a[i] * self.state[-(i + 1)] for i in range(self.k)) + self.c
        next_value %= self.m
        self.state.append(next_value)
        self.state.pop(0)
        return next_value


a = [1, 1]  # Współczynniki dla U_n+1 = U_n + U_n-1
c = 0  # Wartość c
m = 10000  # Modulo m
seed = [1, 1]  # Wartości inicjalizacyjne U1, U2

generator = LinearCongruentialGenerator(a, c, m, seed)
sampels = [m]

for i in range(m):
    sampels.append(generator.next())

# Konwersa danych do zakresu [0, 1]
liczby_01 = konwersja_do_01(sampels, m)

#------------------------wykresy--------------------------

#dystrybuanta
dystrybuanta(liczby_01, 1)

#wykresy kolejnych liczb
# wykres_liczb(liczby)
wykres_liczb(liczby_01)

wykres_punktow(liczby_01)

wykres_punktow_3d(liczby_01)

# --------------------Histogram-------------------------

num_bins = 30
plt.hist(liczby_01, bins=num_bins, edgecolor='green')
plt.title("Histogram wygenerowanych liczb po konwersji")

plt.xlabel("Wartość")
plt.ylabel("Częstotliwość")
plt.show()

#------------------------Testy--------------------------

# test chi_kwadrat
# Wpisz parametr k:
k = 5
statystyka_chi_kwadrat, wartosc_krytyczna = chi_kwadrat(liczby_01, k)
print("---test Chi-kwadrat:---")
print("Statystyka testu chi-kwadrat:", statystyka_chi_kwadrat)
print("Wartość krytyczna dla poziomu istotności 0.05 i", k - 1, "stopni swobody:", wartosc_krytyczna)

#  Kołmogorowa
ks_stat, p_value = test_ks(liczby_01)
print("---test Kołmogrowa:---")
print("Statystyka KS:", ks_stat)
print("Wartość p:", p_value)