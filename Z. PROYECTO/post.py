class Post:
    def __init__(self, publisher, tipo, descripcion, fecha, hashtag, multimedia):
        self.publisher = publisher
        self.tipo = tipo
        self.descripcion = descripcion
        self.fecha = fecha
        self.hashtag = hashtag
        self.multimedia = multimedia
        self.comentario = []
        self.like = []
    
    def mostrar_publi(self):
        print(f"·Publisher: {self.publisher}\n·Tipo: {self.tipo} \n·Descripcion: {self.descripcion}\n·Fecha: {self.fecha}\n·Hashtag: {self.hashtag}\n·Multimedia: {self.multimedia}")
        
    def mostrar__(self):
        print(f"·Publisher: {self.publisher}\n·Hashtag: {self.hashtag}")