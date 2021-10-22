nombre = input('Ingresa el nombre del libro: ')
id = int(input('Ingresa la ID: '))
precio = float(input('Ingresa su precio: '))
envio = input('Indica si el envio es gratuito (True/False): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = bool(input('Valor incorrecto, escribir True o False: '))

print(f'''
Nombre: {nombre} 
ID: {id}
Precio: {precio}
¿Envio Gratis?: {envio}''' )