import math
import matplotlib.pyplot as plt
from scipy.stats import chi2
import numpy as np
from scipy.stats import kstest

# chi_kwadrat
def chi_kwadrat(data, k):
    n = len(data)
    stopnie_swobody = k - 1
    l_obserwacji, _ = np.histogram(data, bins=k)
    l_spodziewanych_obserwacji = np.ones(k) * (n / k)

    statystyka_chi_kwadrat = np.sum((l_obserwacji - l_spodziewanych_obserwacji) ** 2 / l_spodziewanych_obserwacji)

    # Wpisz poziom istotności:
    p_istotnosci = 1 - 0.05
    wartosc_krytyczna = chi2.ppf(p_istotnosci, stopnie_swobody)

    return statystyka_chi_kwadrat, wartosc_krytyczna

#  Kołmogorowa
def dystrybuanta_jednostajna(x):
    return x  # Dystrybuanta rozkładu jednostajnego zakres [0,1]

def test_ks(liczby_01):
    # Obliczanie statystyki KS i wartości p dla danych liczby oraz dystrybuanty jednostajnej
    ks_stat, p_value = kstest(liczby_01, dystrybuanta_jednostajna)
    return ks_stat, p_value