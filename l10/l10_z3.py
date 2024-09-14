# Napisać program, w którym należy utworzysz funkcje czy_liczba_pierwsza(n) sprawdzajacą czy n jest liczbą pierwszą, zwracając True lub False.
# Następnie utwórzyć kolejną funkcję generuj_nieparzyste_liczby_pierwsze() wykorzystującą wcześniej utworzoną funckę czy_liczba_pierwsza(n),
# która za pomocą wyrażania generującego obliczy liczby pierwsze od 1 do 100.
# Wynik wyświetl w postaci listy zawierającej liczby pierwsze ze wskazanego przedziału.

# Sprawdzanie, czy liczba jest pierwsza powinno odbyć się w odrębnej funkcji.
# Tip

# Przykład:
# Nieparzyste liczby pierwsze od 1 do 100:
# [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def czy_liczba_pierwsza(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generuj_nieparzyste_liczby_pierwsze():
    return (i for i in range(3, 101, 2) if czy_liczba_pierwsza(i))

def main():
    print("Nieparzyste liczby pierwsze od 1 do 100:")
    liczby_pierwsze = list(generuj_nieparzyste_liczby_pierwsze())
    print(liczby_pierwsze)

if __name__ == "__main__":
    main()
