# Los diccionarios en Python son una estructura de datos que permite almacenar y organizar datos en pares clave-valor. Cada clave debe ser única, y se utiliza para acceder a su correspondiente valor en el diccionario. Los diccionarios son mutables, lo que significa que se pueden modificar una vez que se crean. Son representados por llaves {} en Python.

dictionary = {
  'Nombre': 'Marvin',
  'Apellido': 'Zuniga',
  'Sexo': 'Masculino',
  'Edad': 34,
  'Estado Civil': 'Casado',
  'Email': 'marvin_zuniga19@outlook.com'
}
# print(dictionary)

# para acceder a un valor del diccionario se utiliza el parentesis cuadrado []

# print(dictionary['Nombre'])

# Tambien podemos usar el metodo get para ser mas especifico

# print(dictionary.get('Edad'))

# si se desea cambiar un valor del diccionario, tambien podemos medir la longitud de un diccionario

dictionary['Estado Civil'] = 'Soltero'

# print(dictionary)
# print(len(dictionary))

# Agregar valores a los Diccionarios

dictionary['Numero de Telefono'] = 83712956
# print(dictionary)

# Eliminar valor dentro del Diccionario

# dictionary.pop('Email')
# print(dictionary)

# pop.item elimina el ultimo valor del diccionario
# dictionary.popitem
# print (dictionary)

# del: Sirve para eliminar valores dentro del diccionario.

del dictionary['Numero de Telefono']
# print(dictionary)

# Generando copias de los Diccionarios.

# copia_dictionary = dictionary.copy()
# print(copia_dictionary)

copia_dictionary = dict(dictionary)
print(copia_dictionary)

# Eliminar todos los valores de un diccionario 
dictionary.clear()
print(dictionary)

# Otra forma de copiar diccionarios

