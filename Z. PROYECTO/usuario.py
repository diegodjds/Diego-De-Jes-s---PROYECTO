class Usuario:
    def __init__(self, id_user, nombre, apellido, correo, user):
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.user = user
        self.peticion = []
        
        
    def mostrar(self):
        print(f"id user: {self.id_user}\nNombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nUsername: {self.user}")
        