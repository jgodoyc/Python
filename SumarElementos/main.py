
def suma(*num):
    resultado = 0
    for i in num:
        resultado += i
    return resultado

total = suma(1,2,3,4,5)
print(total)