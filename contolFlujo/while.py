# "while" evalúa una condición y luego ejecuta un bloque de código si la condición es verdadera. El bloque de código se ejecuta repetidamente hasta que la condición llega ser o es falsa.

contador = 0
while contador < 10:
  print(contador)
  contador += 1
  
  
# Ejemplo  
  
dia = 0
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
while dia  < 7:
  print('hoy es ' + semana[dia])
  dia +=1
  
  '''Explicación línea por línea del CÓDIGO anterior:

La variable "dia" tiene el valor 0.
La variable semana es asignada a una lista que contiene todos los días de la semana.
El bucle while comienza
El bloque de código se ejecutará hasta que la condición devuelva "true".
La condición es 'dia < 7' que aproximadamente dice que se ejecute el bucle while hasta que la variable dia sea menor que 7.
Así que cuando el dia=7 el bucle while deja de ejecutarse.
La variable dia se actualiza en cada iteración.
Cuando el bucle while se ejecuta por primera vez, la línea "Hoy es lunes" se imprime en la consola y la variable dia se hace igual a 1.
Como la variable dia es igual a 1 y es menor que 7, se ejecuta de nuevo el bucle while.
Continúa una y otra vez y cuando la consola imprime 'Hoy es domingo' la variable dia es ahora igual a 7 y el bucle while deja de ejecutarse. '''


'''###################################################################'''

# WHILE: BREAK Y CONTINUE

'''INTRUCCION BREAK '''

# le proporciona la oportunidad de cerrar un bucle cuando se activa una # condición externa. Debe poner la instrucción break dentro del bloque # # de código bajo la instrucción de su bucle

'''Ejemplo'''

number = 0

for number in range(10):
  if number == 5:
    break    # break here

  print('Number is ' + str(number))

print('Out of loop')


'''Instrucción continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.

La instrucción continue se encuentra dentro del bloque de código abajo de la instrucción del bucle, generalmente después de una instrucción if condicional.

Usando el mismo programa de bucle for que en la sección anterior Instrucción break, emplearemos la instrucción continue en vez de la instrucción break '''

# Ejemplo

number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')