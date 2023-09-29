# Usando el codigo de Try_except seguiremos agregando codigo para sumar restar, dividir y multiplicar

primero = input('Ingrese primer numero: ')

try:
  primero = int(primero)
except:
  primero = 'cadena de caracteres'
  
if primero == 'cadena de caracteres':
  print('ingresaste un dato equivocado intenta con numeros')
  exit()
  
segundo = input('ingresa segundo numero: ')

try:
  segundo = int(segundo)
except:
  segundo = 'cadena de caracteres'

if segundo == 'cadena de caracteres':
  print('ingresaste un dato equivocado intenta con numeros')
  exit()
  
symbol = input('Ingrese operacion: ')

if symbol == '+':
  print('Suma:', primero + segundo )
elif symbol == '-':
  print('Resta:', primero - segundo )
elif symbol == '*':
  print('Multiplicacion:', primero * segundo )
elif symbol == '/':
  print('Division:', primero / segundo )
else:
  print('El simbolo ingresado no es valido')

  