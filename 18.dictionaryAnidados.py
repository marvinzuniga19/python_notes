# Diccionarios Anidados son Diccionarios dentro de otros Diccionarios

perros = {
    "danger": {"raza": "doberman", "edad": 2},
    "daiser": {"raza": "bulldog", "edad": 5},
    "et": {"raza": "Bull Terrier", "edad": 10},
    "rambo": {"raza": "Pitbull", "edad": 15},
    "vicky": {"raza": "Chihuahua", "edad": 1},
}
# print(perros)

# Otra manera de hacer diccionarios anidados

danger = {"raza": "doberman", "edad": 3}
kaiser = {"raza": "pitbull", "edad": 5}

dogs = {
    "danger": danger,
    "kaiser": kaiser
}

# print(dogs)


# USO DEL CONSTRUCTOR DIC PARA CREAR DICCIONARIOS

perritos = dict(nombre="jason", edad= 7)
print(perritos)