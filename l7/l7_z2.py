# Zad. 2 Napisać program proszący użytkownika o podanie dwóch liczb a i b i wypisujący ich sumę, różnicę,
# iloczyn, iloraz, √(𝑎 + 𝑏) oraz ab i ba. W przypadku dzielenia przez 0 lub a+b < 0 zwróć wynik jako 'undefined'.
# Przykład:
# Podaj liczbę a: 5
# Podaj liczbę b: 0
# Suma: 5.0
# Różnica: 5.0
# Iloczyn: 0.0
# Iloraz: undefined
# Pierwiastek z (a + b): 2.23606797749979
# a do potęgi b: 1.0
# b do potęgi a: 0.0

import math

# Pobieranie danych od użytkownika
a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))

# Obliczenia
suma = a + b
roznica = a - b
iloczyn = a * b
iloraz = a / b if b != 0 else "undefined"  # Obsługa dzielenia przez zero
pierwiastek = math.sqrt(a + b) if a + b >= 0 else "undefined"  # Obsługa pierwiastka z liczby ujemnej
a_potega_b = a ** b
b_potega_a = b ** a

# Wyświetlanie wyników
print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn: {iloczyn}")
print(f"Iloraz: {iloraz}")
print(f"Pierwiastek z (a + b): {pierwiastek}")
print(f"a do potęgi b: {a_potega_b}")
print(f"b do potęgi a: {b_potega_a}")
