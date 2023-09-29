# El operador and evalúa si el valor a la izquierda y el de la derecha son True, y en el caso de ser cierto, devuelve True. Si uno de los dos valores es False, el resultado será False. 


if 2 < 5 and  3 > 2:
  print('ambas debe devolver True')  # ambas instrucciones deben devolver True porque las condiciones se cumplen
  
  
if 2 < 3 and 3 > 4:
  print('hay una condicion que no se cumple por lo tanto no se imprimira por la terminal') # una de las condiciones no se cumple por lo tanto no se imprime por consola el print.
  
  
# El operador Or, si la evaluacion de la izquierda es true todo se evalua en true y si la evaluacion de la derecha es true toda sera sera tomada como true

if 4 < 5 or 6 <7:
  print('ambas son true')
  
if 7 > 8 or 8 < 9:
  print('no se cumple la condicion de la izquierda, pero si la derecha, se imprime')
  
if 1 < 2 or 2 < 1: # si ninguna se cumple false no se imprime
  print('ninguna condicion se cumple, no se imprime')