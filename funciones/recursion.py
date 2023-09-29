# Recusrsion: La recursión es un concepto matemático y de programación común. Significa que una función se llama a sí misma. Esto tiene el beneficio de significar que puede recorrer los datos para obtener un resultado.

def recursividad(x):
  if(x < 1):
    return x
  print (x)
  recursividad(x - 1)

recursividad(6)

'''
La función recursividad toma un valor x como argumento.
En el primer bloque if, verifica si x es menor que 1. Si es verdadero, la función simplemente devuelve x. Esta es la condición de terminación de la recursión.
Si x no es menor que 1, se ejecuta la instrucción print(x). Esto imprimirá el valor de x en la consola.
Luego, se llama a la función recursividad nuevamente, pasando x - 1 como argumento. Esto es lo que crea el aspecto recursivo del código.
El proceso se repite hasta que x sea menor que 1. En cada iteración, se imprimirá el valor actual de x y se llamará a la función nuevamente con x - 1.
Cuando se llama a recursividad(6) al final del código, aquí está lo que sucede:

x es igual a 6. No es menor que 1, por lo que se imprime 6 y se llama a recursividad(5).
Dentro de la llamada recursividad(5), se imprime 5 y se llama a recursividad(4).
Este proceso se repite hasta que se llega a recursividad(1). Dentro de esta llamada, se imprimirá 1 y luego se llamará a recursividad(0).
Finalmente, en la llamada recursividad(0), la condición (x < 1) es verdadera, por lo que se devuelve 0.
'''