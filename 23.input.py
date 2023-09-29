# input pide al usuario que ingrese valores o datos de algun tipo ya sea numerico o strings

# Ejercicio : pide al usuario que intente adivinar mediante una entrada el nombre de animales dentro de una lista e imprime por consola el resultado.

dogName = input('ingrese nombres de perro: ')

dogList = ['kaiser', 'bobby', 'toby', 'beto', 'pepe']

if dogList.count(dogName) > 0:
  print(f'El nombre del perro existe: , {dogName}')
else:
  print(f'El nombre del perro no existe: , {dogName}')
  






