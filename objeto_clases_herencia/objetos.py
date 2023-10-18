# Clases: es un bloque de código que define un tipo de objeto, así como los métodos y atributos que estarán asociados con ese tipo de objeto.

class Usuario: # clases primer letra mayuscula
    nombre = 'Marvin'
    apellido = 'Zuniga'

usuario = Usuario() # instancia de un usuario, creamos una variable y llamamos a la clase como si fuese una funcion.

print(usuario.nombre, usuario.apellido) # accedemos a la propiedad nombre y llamamos de nuevo a la instancia e ingresamos al elemento apellido