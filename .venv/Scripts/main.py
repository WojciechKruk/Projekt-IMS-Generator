import math
import matplotlib.pyplot as plt
from scipy.stats import chi2
import numpy as np
from scipy.stats import kstest
from funkcje import *
from wykresy import *
from testy import *

# Parametry generatora
seed = 6
a = 1664525
c = 1013904223
m = 2**32
zakres = 2000

# sprawdzanie parametrów
dobor_a(m, a)
dobor_c(m, c)

# Generowanie liczb
#---LCG---
liczby = LCG(seed, a, c, m, zakres)
liczby_01 = konwersja_do_01(liczby, m)

#---Middle Square---
# liczby = middle_square(seed, zakres)
# liczby_01 = liczby

#---Słaby---
# liczby = slaby_generator(seed, zakres)
# liczby_01 = konwersja_do_01(liczby, 16)

#---Oszukany---
# zakres = 1000
# przyrost = 0.37
# liczby_pom = generator_bardzo_pseudolosowy(zakres, przyrost)
# liczby_pom2 = LCG(seed, a, c, m, zakres)
# print(liczby_pom)
# print(len(liczby_pom))
# liczby_pom2.pop(-1)
# liczby = wybierz_losowe(liczby_pom2, liczby_pom, zakres)
# liczby_01 = [liczba / (zakres*przyrost) for liczba in liczby]


# print(liczby)
print(liczby_01)
# print(len(liczby_01))

#------------------------wykresy--------------------------

#dystrybuanta
# dystrybuanta(liczby_01, 1)

#wykresy kolejnych liczb
# wykres_liczb(liczby)
wykres_liczb(liczby_01)

#wykres punktów 2d
# wykres_punktow(liczby_01)

#wykres punktów 2d z przesunięciem
# przesuniecie = 1
# wykres_punktow_przesuniecie(liczby_01, przesuniecie)


#wykres punktów 3d
# wykres_punktow_3d(liczby_01)

#--------------------Histogram-------------------------
# Ustawienie liczby koszyków
num_bins = 40

# plt.hist(liczby, bins=num_bins, edgecolor='black')
# plt.title("Histogram wygenerowanych liczb")

plt.hist(liczby_01, bins=num_bins, edgecolor='green')
plt.title("Histogram wygenerowanych liczb po konwersji")

plt.xlabel("Wartość")
plt.ylabel("Częstotliwość")
plt.show()

#------------------------Testy--------------------------

#Chi_kwadrat
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
