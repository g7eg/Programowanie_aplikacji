# Napisać funkcję kelvin_na_celsiusz() która przyjmuje wartość temperatury w Kelvinach i zwraca wartość wyrażoną w
# stopniach Celsjusza. W przypadku podania wartości ujemnej funkcja zwraca None.


# Przykład:
# Podaj temperaturę w Kelvinach: 223
# Temperatura w stopniach Celsjusza: -50.15

# Przykład:
# Podaj temperaturę w Kelvinach: -2
# Wartość nie może być ujemna.

def kelvin_na_celsiusz(temperatura_kelvin):
    if temperatura_kelvin < 0:
        return None
    return temperatura_kelvin - 273.15

# Testowanie funkcji
if __name__ == "__main__":
    temp_kelvin = float(input("Podaj temperaturę w Kelvinach: "))
    temp_celsiusz = kelvin_na_celsiusz(temp_kelvin)
    if temp_celsiusz is None:
        print("Wartość nie może być ujemna.")
    else:
        print(f"Temperatura w stopniach Celsjusza: {temp_celsiusz:.2f}")
