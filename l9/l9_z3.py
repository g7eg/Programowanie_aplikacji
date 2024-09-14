# Korzystając z programu z zad 1 do wprowadzenia liczb, znaleźć najmniejszą i największą wartość w
# liście i wypisać ją na ekran

# Przykład:
# Ile chcesz wprowadzić liczb? 4
# Podaj liczbę: 2
# Podaj liczbę: 3
# Podaj liczbę: 5
# Podaj liczbę: 6
# Lista: [2, 3, 5, 6]
# Najmniejsza wartość: 2
# Największa wartość: 6

# Przykład:
# Ile chcesz wprowadzić liczb? -2
# Błędna wartość, wprowadź liczbę większą niż 0.

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
        print(f"Najmniejsza wartość: {min(lista)}")
        print(f"Największa wartość: {max(lista)}")
except ValueError:
    print("Błędna wartość, wprowadź liczbę całkowitą.")
