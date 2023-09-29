
""" Una función te permite definir un bloque de código reutilizable que se puede ejecutar muchas veces dentro de tu programa. 


Sintaxis
En Python, una definición de función tiene las siguientes características:

La palabra clave def
Un nombre de función
Paréntesis (), y dentro de los paréntesis los parámetros de entrada, aunque los parámetros de entrada sean opcionales.
Dos puntos :
Algún bloque de código para ejecutar
Una sentencia de retorno (opcional) """

# Ejemplos:

# función sin parámetros o retorno de valores
def diHola():
  print("Hello!")

diHola()  # llamada a la función, 'Hello!' se muestra en la consola


# función con un parámetro
def holaConNombre(name):
  print("Hello " + name + "!")

holaConNombre("Ada")  # llamada a la función, 'Hello Ada!' se muestra en la consola


# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
  return val1 * val2

multiplica(3, 5)  # muestra 15 en la consola


''' Mas ejemplos de Funciones'''
 
def suma(valor1, valor2):
  return valor1 + valor2
print(f'Resultado de la suma en la funcion es: {suma(2,2)}')

''' *arg se utiliza para recibir un numero variable de argumentos
sin palabras clave se debe usar un asterisco antes del nombre del parametro para luego pasar un numero variable de argumentos
La salida hace una tupla
'''


def numeros(*arg):
  print("Este es una funcion", type(arg))
  
numeros('funcion para varias variables')


''' **kwargs nos permite pasar un número variable de argumentos de palabras clave a una función de Python. En la función, utilizamos el doble asterisco (**) antes del nombre del parámetro para denotar este tipo de argumento.
'''

def total_fruta(**kwargs):
  print(kwargs)
  
total_fruta(banana=5, mango=7, apple=8)
  
''' Así vemos que los argumentos, en este caso, se pasan como un diccionario y estos argumentos hacen un diccionario dentro de la función con el nombre igual que el parámetro excluyendo **.'''



''' Pasando una lista como argumento a una funcion'''

def miFuncionLista(lista):
  for elemento in lista:
    print(elemento)

miFuncionLista(['Marvin', 'Zuniga'])



def concatenarNombres(lista):
    i = ' '
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenarNombres(['Chanchito', 'Feliz'])
print(nombres)


# explicacion:

'''
1. Se define una función llamada `concatenarNombres` que toma un argumento llamado `lista`. Esta función tiene la tarea de tomar una lista de nombres y concatenarlos en una cadena de texto.

2. Se inicializa una variable `i` con un espacio en blanco `' '`. Esta variable se usará para acumular los nombres concatenados.

3. Comienza un bucle `for` que recorre cada elemento `el` en la lista proporcionada como argumento a la función.

4. Dentro del bucle, se realiza la concatenación de nombres en la variable `i`. Cada vez que se itera, se agrega el valor de `el` (un nombre) seguido de un espacio en blanco y se asigna el resultado nuevamente a la variable `i`.

5. Una vez que se ha recorrido toda la lista y se han concatenado todos los nombres en la variable `i`, se sale del bucle.

6. Finalmente, la función retorna la cadena resultante `i`, que contiene los nombres concatenados con espacios en blanco entre ellos.

7. Fuera de la definición de la función, se llama a la función `concatenarNombres` con la lista `['Chanchito', 'Feliz']`. Los nombres en la lista serán concatenados con espacios en blanco y el resultado se asignará a la variable `nombres`.

8. Finalmente, se imprime el contenido de la variable `nombres`, que debería mostrar la cadena resultante de la concatenación de los nombres en la lista, separados por espacios en blanco.

En resumen, este código define una función que toma una lista de nombres, los concatena en una cadena de texto con espacios en blanco entre ellos y luego imprime esa cadena resultante. En este caso específico, imprimiría: `" Chanchito Feliz "`.
'''