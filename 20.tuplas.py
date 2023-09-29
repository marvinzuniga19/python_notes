# Tuplas: Son colecciones de datos idénticos o distintos clasificados con un índice y que no pueden ser modificados, si deseas cambiar una tupla tendrias que crear una copia de las misma

tupla1 = (1, 2, 3, 'gato', 'perro')
# print(tupla1.count('perro')) 

# puede usarse el metodo COUNT que cuenta el numero de veces que un dato ha sido escrito en este caso selecione str perro este imprimira 1 en la terminal porque solo esta una vez dentrdo de la tupla.

# print(tupla1.index('gato')) 

# INDEX, nos permite obtener el índice o posición de la primera aparición de un elemento dentro de una lista

# Transformar tupla a lista.

lista = list(tupla1) 
# creamos una variable y le pasamos list para que la tupla se convierta en una lista.

lista.append('kratos') # append agrega str kratos
print(lista.count('gato')) # metodo count cuentas cuantas veces esta el str gato



