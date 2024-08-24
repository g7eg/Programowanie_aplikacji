# Lista 7 Zad. 8
# Napisać program, który pobierze od studenta liczbę punktów i oceni go według podanej skali. Ponadto
# użytkownik może wybrać w jakiej formie chce dostać ocenę (liczbowo lub słownie lub oba). W przypadku podania błędnej formy wypisz kompunikat: 'Nieznana forma oceny.'
# Skala:
# <0; 50) 2.0 (niedostateczny)
# <50;60) 3.0 (dostateczny)
# <60;70) 3.5 (dostateczny plus)
# <70;80) 4.0 (dobry)
# <80;90) 4.5 (dobry plus)
# <90;100) 5.0 (bardzo dobry)
# <100> 5.5 (celujący)
# Przykład:
# Podaj liczbę punktów: 66
# Wybierz formę oceny (liczbowo, słownie, oba): liczbowo
# Otrzymałeś ocenę: 3.5
# Przykład:
# Podaj liczbę punktów: 99
# Wybierz formę oceny (liczbowo, słownie, oba): oba
# Otrzymałeś ocenę: 5.0 (bardzo dobry)

# Pobieranie danych od użytkownika
punkty = float(input("Podaj liczbę punktów: "))
forma_oceny = input("Wybierz formę oceny (liczbowo, słownie, oba): ").strip().lower()

# Ocena na podstawie punktów
if punkty < 0 or punkty > 100:
    ocena_liczbowa = 5.5
    ocena_slowna = "celujący"
elif punkty < 50:
    ocena_liczbowa = 2.0
    ocena_slowna = "niedostateczny"
elif punkty < 60:
    ocena_liczbowa = 3.0
    ocena_slowna = "dostateczny"
elif punkty < 70:
    ocena_liczbowa = 3.5
    ocena_slowna = "dostateczny plus"
elif punkty < 80:
    ocena_liczbowa = 4.0
    ocena_slowna = "dobry"
elif punkty < 90:
    ocena_liczbowa = 4.5
    ocena_slowna = "dobry plus"
else:
    ocena_liczbowa = 5.0
    ocena_slowna = "bardzo dobry"

# Wyświetlenie oceny w wybranej formie
if forma_oceny == "liczbowo":
    print(f"Otrzymałeś ocenę: {ocena_liczbowa}")
elif forma_oceny == "słownie":
    print(f"Otrzymałeś ocenę: {ocena_slowna}")
elif forma_oceny == "oba":
    print(f"Otrzymałeś ocenę: {ocena_liczbowa} ({ocena_slowna})")
else:
    print("Nieznana forma oceny.")
