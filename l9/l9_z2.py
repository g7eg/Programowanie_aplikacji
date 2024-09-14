# Korzystając z programu z zad 1 do wprowadzenia liczb, zsumować wszystkie liczby w liście i wypisać na ekran.

# Przykład:
# Ile chcesz wprowadzić liczb? 3
# Podaj liczbę: 2
# Podaj liczbę: 3
# Podaj liczbę: 5
# Lista: [2, 3, 5]
# Suma liczb: 10

# Prośba o ilość liczb i sumowanie ich
try:
    n = int(input("Ile chcesz wprowadzić liczb? "))
    if n <= 0:
        print("Błędna wartość, wprowadź liczbę większą niż 0.")
    else:
        lista = []
        for i in range(n):
            liczba = int(input("Podaj liczbę: "))
            lista.append(liczba)
        suma = sum(lista)
        print(f"Lista: {lista}")
        print(f"Suma: {suma}")
except ValueError:
    print("Błędna wartość, wprowadź liczbę całkowitą.")
