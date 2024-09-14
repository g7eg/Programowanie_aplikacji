# Lista 8 Zad. 7
# Napisać program który wypisze na ekranie wszystkie możliwe kombinacje książek jakie można wybrać.
# Do wyboru jest pięć książek, a wybieramy trzy z nich. Fragment danych jakie powinny zostać
# wypisywane na ekranie:
# 1 2 3
# 1 2 4
# 1 2 5
# …


import itertools

# Lista książek od 1 do 5
ksiazki = [1, 2, 3, 4, 5]

# Generowanie wszystkich kombinacji 3 książek z 5
kombinacje = itertools.combinations(ksiazki, 3)

# Wypisywanie każdej kombinacji
for kombinacja in kombinacje:
    print(" ".join(map(str, kombinacja)))
