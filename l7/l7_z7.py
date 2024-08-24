# Lista 7 Zad. 7
# Napisać program, który sprawdzi czy z podanych długości można stworzyć trójkąt i wypisze odpowiedni
# komunikat.
# Przykład:
# Podaj długość pierwszego boku: 1
# Podaj długość drugiego boku: 2
# Podaj długość trzeciego boku: 3
# Nie można stworzyć trójkąta.
# Przykład:
# Podaj długość pierwszego boku: 3
# Podaj długość drugiego boku: 4
# Podaj długość trzeciego boku: 5
# Można stworzyć trójkąt.


# Pobieranie długości boków od użytkownika
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

# Sprawdzanie, czy można utworzyć trójkąt
if a + b > c and a + c > b and b + c > a:
    print("Można stworzyć trójkąt.")
else:
    print("Nie można stworzyć trójkąta.")
