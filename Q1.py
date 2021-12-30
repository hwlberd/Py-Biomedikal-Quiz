# değerler diziye kayıt ediliyor

from math import log


def entropy_Calculation():
    x = [
        ['A', '-', 'T', 'T', 'G', '-', 'C', 'T', 'T'],
        ['A', 'C', 'C', 'T', 'G', 'G', 'C', '-', 'T'],
        ['A', 'C', 'T', 'A', '-', 'G', 'C', 'T', 'A'],
        ['A', 'G', 'T', 'A', 'G', 'C', 'A', 'T', 'T']
    ]

    # Tekrar sayıları 0 olarak başlatılıyor

    # Dizideki her sutündaki tekrar sayıları hesaplanıyor
    for i in range(9):
        a = 0.0
        c = 0.0
        g = 0.0
        t = 0.0
        minus = 0.0
        entropy = 0.0
        for j in range(4):
            if x[j][i] == 'A':
                a += 1
            if x[j][i] == 'C':
                c += 1
            if x[j][i] == 'G':
                g += 1
            if x[j][i] == 'T':
                t += 1
            if x[j][i] == '-':
                minus += 1

        print(i + 1, '. ci sütun için ', 'pA =', a / 4, 'pT =', t / 4, 'pC =', c / 4, 'pG =', g / 4, 'p_ =', minus / 4)

        if (a / 4) <= 0:
            entropy += 0
        else:
            entropy += (a / 4) * log(a / 4, 10)
        if (t / 4) <= 0:
            entropy += 0
        else:
            entropy += (t / 4) * log(t / 4, 10)
        if (c / 4) <= 0:
            entropy += 0
        else:
            entropy += (c / 4) * log(c / 4, 10)
        if (g / 4) <= 0:
            entropy += 0
        else:
            entropy += (g / 4) * log(g / 4, 10)
        if (minus / 4) <= 0:
            entropy += 0
        else:
            entropy += (minus / 4) * log(minus / 4, 10)
        print("Entropy = ", -entropy)


entropy_Calculation()
