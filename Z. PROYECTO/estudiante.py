from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, id_user, nombre, apellido, correo, user, carrera, followers):
        super().__init__(id_user, nombre, apellido, correo, user)
        self.carrera = carrera
        self.followers = followers
        
    def mostrar(self):
        print(f"id user: {self.id_user}\nNombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nUsername: {self.user}\nCarrera: {self.carrera}\nFollowers: {self.followers}")
    
    def solo_mostrar(self):
        print(f"Nombre: {self.nombre}\nUsername: {self.user}")