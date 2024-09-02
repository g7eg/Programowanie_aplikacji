# Lista 8 Zad. 1
# Napisać program, który dla wprowadzonego przez użytkownika ciągu liczb rzeczywistych wyznacza ich
# średnią arytmetyczną. Wprowadzanie ciągu kończy się poprzez wprowadzenie napisu ’end’. Program
# powinien raportować błąd, jeśli ’end’ jest pierwszą podaną wartością. Przykładowo, dla wejścia:
# 1
# -22
# 8
# -3.5
# 13
# end
# Poprawną odpowiedzią jest -0.7.

# Inicjalizacja listy do przechowywania liczb
liczby = []

while True:
    wejscie = input("Podaj liczbę (lub 'end' aby zakończyć): ")

    if wejscie == 'end':
        if not liczby:
            print("Błąd: 'end' nie może być pierwszą podaną wartością.")
            break
        else:
            srednia = sum(liczby) / len(liczby)
            print(f"Średnia arytmetyczna wynosi: {srednia}")
            break
    else:
        try:
            liczba = float(wejscie)
            liczby.append(liczba)
        except ValueError:
            print("Błąd: Wprowadzono nieprawidłową wartość.")
