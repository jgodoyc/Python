#def listarNombres(*nombres):
 #   for nombre in nombres:
  #      print(nombre)


#listarNombres('Javier', 'Eduardo', 'Bastian', 'Nicolas')


#                      Argumentos llave-valor
#def listarTerminos(**terminos):
 #   for llave, valor in terminos.items():
  #      print(f'{llave}: {valor}')

#listarTerminos(OTPP= 'Organizacion de Tomateras y Pipa de la Paz')





# ------------------- RECURSIVO -------------------------------
def factorial(numero)
    if numero == 1:
        return 1
    else:
         return numero * factorial(numero-1)