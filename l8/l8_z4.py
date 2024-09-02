k = int(input("Podaj liczbę całkowitą k: "))

if k <= 0:
    print("Błąd: Liczba k musi być większa od zera.")
else:
    for i in range(50, 101):
        if i % k == 0:
            print(i)
