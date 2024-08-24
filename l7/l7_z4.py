# Lista 7 Zad. 4
# Napisać program proszący użytkownika o podanie dwóch liczb a i b. Następnie należy wyświetlić, która
# z tych liczb jest większa, bądź komunikat, że są sobie równe.
# Przykład:
# Podaj pierwszą liczbę (a): 2
# Podaj drugą liczbę (b): 2
# Liczby są sobie równe.
# Przykład:
# Podaj pierwszą liczbę (a): -2
# Podaj drugą liczbę (b): 2
# Liczba 2.0 jest większa od -2.0.

# Pobieranie liczb od użytkownika
a = float(input("Podaj pierwszą liczbę (a): "))
b = float(input("Podaj drugą liczbę (b): "))

# Porównanie liczb
if a > b:
    print(f"Liczba {a} jest większa od {b}.")
elif b > a:
    print(f"Liczba {b} jest większa od {a}.")
else:
    print("Liczby są sobie równe.")
