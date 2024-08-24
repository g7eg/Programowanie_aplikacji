# Lista 7 Zad. 3
# Napisać program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika. Promień
# nie może być ujemny. W przypadku podania liczby ujemnej, program powinien wypisywać komunikat "Błąd: Promień nie może być ujemny." informujący o błędnej wartości i nic nie liczyć.
# Przykład:
# Podaj promień koła: 12
# Pole koła: 452.3893421169302
# Obwód koła: 75.39822368615503
# Przykład:
# Podaj promień koła: -12
# Błąd: Promień nie może być ujemny.

import math

# Pobieranie promienia od użytkownika
radius = float(input("Podaj promień koła: "))

# Sprawdzenie, czy promień jest nieujemny
if radius < 0:
    print("Błąd: Promień nie może być ujemny.")
else:
    # Obliczanie pola i obwodu koła
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    # Wyświetlanie wyników
    print(f"Pole koła: {area}")
    print(f"Obwód koła: {circumference}")
