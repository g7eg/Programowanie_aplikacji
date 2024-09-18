def dodaj_wielomiany(w1, w2):
    # Dopasowanie długości wielomianów przez dodanie zer
    if len(w1) < len(w2):
        w1 = [0] * (len(w2) - len(w1)) + w1
    elif len(w2) < len(w1):
        w2 = [0] * (len(w1) - len(w2)) + w2
    # Dodawanie wielomianów
    return [a + b for a, b in zip(w1, w2)]

def odejmij_wielomiany(w1, w2):
    # Dopasowanie długości wielomianów przez dodanie zer
    if len(w1) < len(w2):
        w1 = [0] * (len(w2) - len(w1)) + w1
    elif len(w2) < len(w1):
        w2 = [0] * (len(w1) - len(w2)) + w2
    # Odejmowanie wielomianów
    return [a - b for a, b in zip(w1, w2)]

def pomnoz_wielomiany(w1, w2):
    # Mnożenie wielomianów
    wynik = [0] * (len(w1) + len(w2) - 1)
    for i in range(len(w1)):
        for j in range(len(w2)):
            wynik[i + j] += w1[i] * w2[j]
    return wynik

def main():
    # Przykładowe wielomiany
    wielomian_1 = [2, -3, 0, 4]  # 2x**3 - 3x**2 + 4
    wielomian_2 = [1, 5, 2]  # x**2 + 5x + 2

    # Dodawanie
    suma = dodaj_wielomiany(wielomian_1, wielomian_2)
    print(f"Suma wielomianów: {suma}")

    # Odejmowanie
    roznica = odejmij_wielomiany(wielomian_1, wielomian_2)
    print(f"Różnica wielomianów: {roznica}")

    # Mnożenie
    iloczyn = pomnoz_wielomiany(wielomian_1, wielomian_2)
    print(f"Iloczyn wielomianów: {iloczyn}")

if __name__ == "__main__":
    main()
