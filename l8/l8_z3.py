# Lista 8 Zad.3 
# Napisać program wyświetlający liczby całkowite z przedziału <x,y> (liczby całkowite x i y podajeużytkownik). 
# W przypadku podania niewłaściwej wartości wyświetl komunikat: "Błąd: Liczba x musi być mniejsza lub równa liczbie y."

x = int(input("Podaj liczbę całkowitą x: "))
y = int(input("Podaj liczbę całkowitą y: "))

if x > y:
    print("Błąd: Liczba x musi być mniejsza lub równa liczbie y.")
else:
    for i in range(x, y + 1):
        print(i)
