def celsius_fahr(temp):
    return temp * 9/5 + 32

def fahr_celsius(temp):
    return (temp-32)* 5/9

temperatura = float(input('Ingresa la temperatura en Celsius: '))
print(celsius_fahr(temperatura))

temperatura = float(input('Ingresa la temperatura en Fahrenheit: '))
print(fahr_celsius(temperatura))