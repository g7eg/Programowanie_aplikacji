# Zad. 1 Napisać program proszący użytkownika o imię i rok urodzenia, a następnie obliczający i wypisujący jego wiek. 
# Przykładowe wykonanie: 
# Podaj swoje imię: Siemomysł 
# Podaj rok urodzenia: 1989 
# Siemomysł, masz 33 lata.

# Pobieranie danych od użytkownika
imie = input("Podaj swoje imię: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))

# Obliczenie wieku
aktualny_rok = 2024  # Możesz dostosować ten rok do aktualnego
wiek = aktualny_rok - rok_urodzenia

# Wyświetlenie wyniku
print(f"{imie}, masz {wiek} lat.")