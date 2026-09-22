

# usuario = {
#     "nombre": "Juan",
#     "edad": 30,
#     "email": "juan@example.com"
# }

# json_string = json.dumps(usuario)
# print(json_string)  # Imprime el JSON como una cadena

# with open('usuario.json', 'w', encoding='utf-8') as archivo:
#     json.dump(usuario, archivo)  # Guarda el JSON en un archivo


# class Post:

#     def __init__(self,titulo,autor,contenido):

#         self.titulo = titulo

#         self.autor = autor

#         self.contenido = contenido

#         self.estado = "Borrador"

#     def publicar(self):

#         self.estado = "Publicado"

        

    

#     def editar_titulo(self,nuevo_titulo):

#         self.titulo = nuevo_titulo

    

#     def mostar_info(self):

#         print(f"Titulo: {self.titulo}")

#         print(f"Autor: {self.autor}")

#         print(f"Contenido: {self.contenido}")

#         print(f"Estado: {self.estado}")

# post_1 = Post("Aprendiendo clases","Camila","En este post bla bla bla")

# post_2 = Post("Prueba","Benicio","Es diferente el contenido")

# post_1.publicar()

 

# print(post_1.titulo)

# print(post_1.autor)

# print(post_1.contenido)

# print(post_1.estado)

# print(post_2.titulo)

# post_1.titulo = "Nuevo titulo"

# print(post_1.titulo)

# post_1.editar_titulo("Titulo editado desde un metodo")

# print(post_1.titulo)

# post_1.mostar_info()

import json

class Productos:
    
    def __init__(self,nombre,precio,cantidad):

        self.nombre = nombre

        self.precio = precio

        self.cantidad = cantidad

    producto_1 = Productos("Camisa", 20.99, 10)
    producto_2 = Productos("Pantalón", 35.50, 5)
    producto_3 = Productos("Zapatos", 50.00, 8)
    productos = [producto_1, producto_2, producto_3]
    
with open('productos.json', 'r', encoding='utf-8') as archivo:
    datos_json = json.load(archivo)

print(datos_json)
    