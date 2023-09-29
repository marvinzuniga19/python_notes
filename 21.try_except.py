# Creamos un script que sume dos numero utilizando input

# los 'try'  te permite probar un bloque de código para errores.
# los 'except'  te permite manejar el error. 

# dato1 = int(input('ingrese numero: ')) 
# dato2 = int(input('ingrese segundo numero:')) 
# print(dato1+dato2)


# Los try generará una excepción, porque 'x' no está definido:
# try:
  # print(x)
# except:
  # print("An exception occurred")  
# Como el bloque de prueba plantea un error, se ejecutará el bloque excepto.

# Otro egemplo
# try:
  # print(x)
# except:
  # print('Variable No definida')
  
  
# Otro Ejemplo.

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
  
print(primero + segundo)
