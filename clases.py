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

    

#     def mostrar_info(self):

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

# post_1.mostrar_info()

class Usuario:

    def __init__(self,username,email,nombre):

        self.username = username

        self.email = email

        self.__nombre = nombre

    def mostrar_perfil(self):

        print("Usuario:",self.username)

        print("Email:",self.email)

        #print("Nombre:",self.nombre)

    

    def get_nombre(self):

        return self.__nombre

    

    def set_nombre(self,nuevo_nombre):

        if nuevo_nombre != "":

            self.__nombre = nuevo_nombre

        else:

            print("El nombre no puede estar vacio")

    

    def presentarse(self):

        print("Hola soy un USUARIO")

class Administrador(Usuario):

    def eliminar_usuario(self):

        print("El administrador elimino un usuario")

    

    def presentarse(self):

        print("Hola soy un ADMIN")

class Autor(Usuario):

    def crear_post(self):

        print("El autor creo un post")

    

    def presentarse(self):

        print("Hola soy un AUTOR")

class Post:

    def __init__(self,titulo,contenido,autor):

        self.titulo = titulo

        self.contenido = contenido

        self.autor = autor

        self.estado = "borrador"

    def publicar(self):

        self.estado = "publicado"

        print("El post ha sido publicado")

    

    def mostrar_resumen(self):

        print("Titulo:",self.titulo)

        print("Contenido:",self.contenido)

        #print("Autor:",self.autor.nombre)

        print("Estado:",self.estado)

 

 

usuario1 = Usuario("arenabelu","cami@coder.com,","Camila")

#usuario1.mostrar_perfil()

post1 = Post("Mi primer post","Este es el contenido",usuario1)

post2 = Post("Mi segundo post","Este es el segundo post",usuario1)

#print(post1.autor.nombre)

#print(usuario1.get_nombre())

#usuario1.set_nombre("Belu")

#print(usuario1.get_nombre())

admin = Administrador("Valen_Tina","val@gmail.com","Valen")

autor = Autor("Javi.R","javir@gmail.com","Javier")

#Probamos la herencia

#admin.mostrar_perfil()

#autor.mostrar_perfil()

#Probar los metodos propios de cada clase

#admin.eliminar_usuario()

#autor.crear_post()

#Probamos el polimorfismo

#admin.presentarse()

#autor.presentarse()

usuarios =[

    admin,

    autor

]

for usuario in usuarios:

    usuario.presentarse()