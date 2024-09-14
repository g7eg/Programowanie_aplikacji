# Lista 8 Zad. 2
# Napisać program wyświetlający liczby całkowite z przedziału <0,y> (liczbę całkowitą y podaje użytkownik). 
# W przypadku podania niewłaściwej wartości wyświetl komunikat: "Błąd: Liczba y musi być większa lub równa 0."

# Przykład:
# Podaj liczbę całkowitą y: 2
# 0
# 1
# 2


y = int(input("Podaj liczbę całkowitą y: "))

if y < 0:
    print("Błąd: Liczba y musi być większa lub równa 0.")
else:
    for i in range(0, y + 1):
        print(i)
