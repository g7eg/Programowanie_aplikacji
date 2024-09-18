# Napisać program, który będzie obliczał i zwracał silnię podanej liczby za pomocą funkcji oblicz_silnie(n). Następnie wykorzystać
# funkcję obliczającą silnię do znalezienia silni dla liczby wybranej przez użytkownika.

# Przykład:
# Podaj liczbę, dla której chcesz obliczyć silnię: 3
# Silnia liczby 3 wynosi 6.

def oblicz_silnie(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

def main():
    try:
        liczba = int(input("Podaj liczbę, dla której chcesz obliczyć silnię: "))
        silnia = oblicz_silnie(liczba)
        if silnia is not None:
            print(f"Silnia liczby {liczba} wynosi {silnia}.")
        else:
            print("Silnia jest niezdefiniowana dla liczb ujemnych.")
    except ValueError:
        print("Podaj poprawną liczbę całkowitą.")

if __name__ == "__main__":
    main()
