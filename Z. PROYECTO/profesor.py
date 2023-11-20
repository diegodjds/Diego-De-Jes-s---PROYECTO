from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, id_user, nombre, apellido, correo, user, departamento, followers ):
        super().__init__(id_user, nombre, apellido, correo, user)
        self.departamento = departamento
        self.followers = followers
        
    def mostrar(self):
        print(f"id user: {self.id_user}\nNombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nUsername: {self.user}\nDepartamento: {self.departamento}\nFollowers: {self.followers}")

    def solo_mostrar(self):
        print(f"Nombre: {self.nombre}\nUsername: {self.user}")