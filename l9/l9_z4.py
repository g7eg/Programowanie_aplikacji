# Korzystając z programu z zad 1 do wprowadzenia liczb, znaleźć wszystkie pary liczb, których w suma
# daje liczbę podaną przez użytkownika.

# Przykład:
# Ile chcesz wprowadzić liczb? 5
# Podaj liczbę: 3
# Podaj liczbę: 4
# Podaj liczbę: 0
# Podaj liczbę: 7
# Podaj liczbę: 1
# Lista: [3, 4, 0, 7, 1]
# Wprowadź szukaną sumę: 7
# 3 + 4 = 7
# 0 + 7 = 7


# Prośba o ilość liczb
try:
    n = int(input("Ile chcesz wprowadzić liczb? "))
    if n <= 0:
        print("Błędna wartość, wprowadź liczbę większą niż 0.")
    else:
        lista = []
        for i in range(n):
            liczba = int(input("Podaj liczbę: "))
            lista.append(liczba)
        print(f"Lista: {lista}")

        # Wprowadzenie szukanej sumy
        suma_szukana = int(input("Wprowadź szukaną sumę: "))

        # Znalezienie par liczb, których suma jest równa szukanej sumie
        znalezione_pary = []
        for i in range(len(lista)):
            for j in range(i + 1, len(lista)):
                if lista[i] + lista[j] == suma_szukana:
                    znalezione_pary.append((lista[i], lista[j]))

        # Wyświetlenie wyników
        if znalezione_pary:
            for para in znalezione_pary:
                print(f"{para[0]} + {para[1]} = {suma_szukana}")
        else:
            print("Brak par liczb, których suma jest równa szukanej sumie.")

except ValueError:
    print("Błędna wartość, wprowadź liczbę całkowitą.")
