''' FOR Se usa para iterar en listas y tuplas, secuencia de datos''' 

''' usuarios  = ['felipe', 'roberto', 'Nicolas']

for usuario in usuarios:
  print(usuario) '''
  
# Usando For con Strings

# usuario = 'Marvin Zuniga'

# for c in usuario:
  # print(c) # imprime 'c' por caracter, itera por cada caracter del string
  
  
# Ejemplo:

usuario = ['Mario', 'Fatima', 'Aracely', 'Karen']

for user in usuario:
  if user == 'Aracely':
    break
  print(user) 
  
# Puedes usar Break, Continue y Pass

# Usando range en FOR 

for x in range(3, 40, 5):
  print(x)
else:
  print('Terminado')
  
# Este ultimo bloque de codigo imprime en el rango del 3 al 40 de 5 en cinco.
