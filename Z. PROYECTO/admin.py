from usuario import Usuario

class Admin(Usuario):
    def __init__(self, id_user, nombre, apellido, correo, user, admin, followers):
        super().__init__(id_user, nombre, apellido, correo, user)
        
        self.admin = admin
        self.followers = followers
    
    def mostrar(self):
        print(f"id user: {self.id_user}\nNombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nUsername: {self.user}\nEspecialidad: {self.admin}\nFollowers: {self.followers}")