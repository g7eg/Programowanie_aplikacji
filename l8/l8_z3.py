# Lista 8 Zad.3 
# Napisać program wyświetlający liczby całkowite z przedziału <x,y> (liczby całkowite x i y podajeużytkownik). W przypadku podania niewłaściwej wartości wyświetl komunikat: "Błąd: Liczba x musi być mniejsza lub równa liczbie y."
# > Przykład:
# Podaj liczbę całkowitą x: -2
# Podaj liczbę całkowitą y: 5
# -2
# -1
# 0
# 1
# 2
# 3
# 4
# 5

# > Przykład:
# Podaj liczbę całkowitą x: 4
# Podaj liczbę całkowitą y: 2
# Błąd: Liczba x musi być mniejsza lub równa liczbie y.


x = int(input("Podaj liczbę całkowitą x: "))
y = int(input("Podaj liczbę całkowitą y: "))

if x > y:
    print("Błąd: Liczba x musi być mniejsza lub równa liczbie y.")
else:
    for i in range(x, y + 1):
        print(i)
