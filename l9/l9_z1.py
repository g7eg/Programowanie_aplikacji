# Lista 9 Zad. 1
# Napisać program proszący użytkownika o ilość liczb, które chce wprowadzić, następnie po kolei, każdą
# liczbę należy wprowadzić do listy i wypisać cała zawartość listy. W przypadku podania niepoprawnej
# wartości w pierwszym pytaniu program powinien powiadomić użytkownika o błędzie.

# Przykład:
# Ile chcesz wprowadzić liczb? 3
# Podaj liczbę: 12
# Podaj liczbę: 33
# Podaj liczbę: 2
# Lista: [12, 33, 2]


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
except ValueError:
    print("Błędna wartość, wprowadź liczbę całkowitą.")
