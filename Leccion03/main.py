mes = int(input('Ingresa mes del año: '))
estacion = None

if mes >= 1 and mes <= 3:
    estacion = 'Verano'
elif mes >=4 and mes <= 6:
    estacion = 'Otoño'
elif mes >=7 and mes <= 9:
    estacion = 'Invierno'
elif mes >= 10 and mes<= 12:
    estacion = 'Primavera'
else:
    estacion = 'Mes incorrecto'

print(estacion)