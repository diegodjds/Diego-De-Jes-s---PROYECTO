from admin import Admin
from post import Post
from estudiante import Estudiante
from profesor import Profesor
import random
import requests
import json

def api_usuarios():
    database = []
    api_users = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json").json()
    for user in api_users:
            if user.get('department'): 
                database.append(Profesor(user["id"], user['firstName'], user['lastName'] , user['email'], user['username'], user['department'], user["following"]) )
            else: 
                database.append(Estudiante(user["id"], user['firstName'], user['lastName'] , user['email'], user['username'], user['major'], user["following"]) )
    
    return database

def api_publicaciones():
    database=[]   
    api_post = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json").json()
    for post in api_post:
            database.append(Post(post["publisher"], post["type"], post["caption"], post["date"], post["tags"], post["multimedia"]))
    
    return database
        



def main():
    
    
    print("\n==============================")
    print("<<<<Bienvenido a METROGRAM>>>>")
    print("==============================")
    
    info_usuarios = api_usuarios()
    info_publicaciones = api_publicaciones()
    user_self=""

    
        
    while True:         
        opcion = input("\n‣Seleccione una opción: \n(1) Registrar usuario. \n(2) Iniciar sesión. \n>> ")
        
        if opcion == "1":
            
            id = random.randint(0,20000)
            
            nombre = input("\n·Ingrese su nombre: ")
            
            while(not nombre.isalpha() or nombre == ""):
                print("Su nombre no puede tener numeros o estar vacio!")
                nombre = input("Ingrese su nombre correctamente >>> ")
            
            apellido = input("·Ingrese su apellido: ")                   
            correo = input("·Ingrese su correo electrónico: ")
            user = input("·Crea tu username: ")
            tipo = input("\n¿Eres estudiante o profesor? \n(1) Estudiante \n(2) Profesor \n(3) Admin \n>>  ")
            
            if tipo == "1":
                tipo = "Estudiante"
                carrera = input("\n¿Qué carrera cursa?: ")
                print("\n【¡Cuenta creada exitosamente!】")
                estudiante1 = Estudiante(id, nombre, apellido, correo, user, carrera, [] )
                info_usuarios.append(estudiante1)
            
                
            elif tipo == "2":
                tipo = "Profesor"
                departamento = input("\n¿Qué departamento pertenece?: ")
                print("\n【¡Cuenta creada exitosamente!】")
                profesor = Profesor(id, nombre, apellido, correo, user, departamento, [] )
                info_usuarios.append(profesor)
            
            elif tipo == "3":
                tipo = "Admin"
                especialidad = input("\nIngrese especialidad: ")
                print("\n【¡Cuenta creada exitosamente!】")
                admin = Admin(id, nombre, apellido, correo, user, especialidad, [])
                info_usuarios.append(admin)
                            
                
            
                    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif opcion == "2":
            while True:
                usuario = input("\nInicia sesión como usuario: ")
                for perfil in info_usuarios:
                    if perfil.user == usuario:
                        user_self = perfil
                        print(f"\nBievenido {perfil.user}")
                        break
                    
                if not user_self:
                    print("\nUsuario no existente.")
                else:
                    break
            break            
        
    while True:
        menu = input("""\n(1) Gestión de perfil \n(2) Gestión de multimedia \n(4) Salir. \n>> """) 
        if menu == "4":
            print("\nSaliendo...")
            break
        
        if menu == "1":

            opcion1 = input("""\n(1) Buscar perfiles. \n(2) Cambiar la información personal de la cuenta.
(3) Borrar los datos de la cuenta. \n(4) Acceder a una cuenta\n>>""")
        
            if opcion1 == "1":
                
                while True:
                    elige = input("\nElige de qué forma desea buscar. \n(1) Username \n(2) Especialidad\n>> ")
                
                    if elige == "1":
                        username = input("\nIngrese el username: ")
                        coincidencias = False
                        for perfil in info_usuarios:
                            if perfil.user == username:
                                coincidencias = True
                                print("\n✓ Se ha encontrado al usuario\n")
                                perfil.mostrar()
                                
                                coincidencias = False
                                print("\n❏ Este es el listado de sus publicaciones")
                                for post in info_publicaciones:
                                        if post.publisher == perfil.id_user:
                                            coincidencias = True
                                            print("\n")
                                            post.mostrar_publi()
                                            seguir = input("\n¿Desea seguir esta cuenta? \n1- Si \n2- No \n>> ")
                                            if seguir == "1":
                                                user_self.followers.append(perfil.id_user)
                                                break
                                            else:
                                                break
                                
                        if coincidencias == False:
                            print("\nError, no se encontraron coincidencias.")
                            break
                        
                    
                    
                    elif elige == "2":
                        especialidad = input("\nIngrese la especialidad: ")
                        print("\nEstos son todos los resultados de esa carrera:\n")
                        coincidencias = False
                        for perfil in info_usuarios:
                            if isinstance(perfil, Estudiante):
                                if perfil.carrera == especialidad:
                                    print("\n")
                                    perfil.mostrar()
                                    coincidencias = True    
                            
                            elif isinstance(perfil, Profesor):
                                if perfil.departamento == especialidad:
                                    print("\n")
                                    perfil.mostrar()
                                    coincidencias = True
                                    
                        if coincidencias == False:
                            print("Error. No se encontraron coincidencias.")            

                    select = input("\n¿Volver a buscar?: \n1- Si \n2- No \n==>")
                    if select == "2":
                        break                   
                
            
# #-------------------------------------------------------------------------------------------------------------------------------------------------------------------                                       
            elif opcion1 == "2":
                
                while True:
                    select = input("\n¿Qué dato deseas cambiar? \n1-Nombre\n2-Apellido\n3-Correo\n4-Username\n5-Especialidad\n==>")
                
                    if select == "1":
                        nombre = input("\nIngrese nuevo nombre: ")
                        for perfil in info_usuarios:
                                if perfil.nombre == user_self.nombre:
                                    perfil.nombre = nombre
                                    print("\nSu nuevo nombre ahora es: " + perfil.nombre + "\n")
                                    perfil.mostrar()
                                    break
                    
                    elif select == "2":
                        apellido = input("\nIngrese nuevo apellido: ")
                        for perfil in info_usuarios:
                            if perfil.apellido == user_self.apellido:
                                perfil.apellido = apellido
                                print("\nSu nuevo apellido ahora es: " + perfil.apellido + "\n")
                                perfil.mostrar()
                                break


                    elif select == "3":
                        correo = input("\nIngrese nuevo correo: ")
                        for perfil in info_usuarios:
                            if perfil.correo == user_self.correo:
                                perfil.correo = correo
                                print("\nSu nuevo correo ahora es: " + perfil.correo + "\n")
                                perfil.mostrar()
                                break


                    elif select == "4":
                        username = input("\nIngrese nuevo username: ")
                        for perfil in info_usuarios:
                            if perfil.user == user_self.user:
                                perfil.user = username
                                print("\nSu nuevo correo ahora es: " + perfil.user + "\n")
                                perfil.mostrar()
                                break


                    elif select == "5":
                        especialidad = input("\nIngrese nueva especialidad: ")
                        for perfil in info_usuarios:
                            if perfil == user_self:
                                if isinstance(perfil,Estudiante):
                                    perfil.carrera = especialidad
                                    print("\nSu nueva carrera ahora es: " + perfil.carrera + "\n")
                                    perfil.mostrar()
                                    break
                                
                                elif isinstance(perfil, Profesor):
                                    perfil.departamento = especialidad
                                    print("\nSu nuevo departamento ahora es: " + perfil.departamento + "\n")
                                    perfil.mostrar()
                                    break
                                
                                elif isinstance(perfil, Admin):
                                    perfil.admin = especialidad
                                    print("\nError. Su única especialidad es administrador.")
                                    perfil.mostrar()
                                    break
                    
                    regresar = input("\n¿Volver a cambiar otros datos? \n1- Si \n2- No\n>>")
                    if regresar == "2":
                        break
    
                        
# #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                      
            elif opcion1 == "3":
                
                while True:
                    borrar = input("\n¿Qué datos deseas borrar?\n1-Nombre\n2-Apellido\n3-Correo\n4-Username\n5-Especialidad\n==>")
                    
                    if borrar == "1":
                        for perfil in info_usuarios:
                            if perfil.user == user_self.user:
                                perfil.nombre = ""
                                print("Se ha borrado el nombre.\n")
                                perfil.mostrar()
                                break                   
                                
                    elif borrar == "2":
                        for perfil in info_usuarios:
                            if perfil.user == user_self.user:
                                perfil.apellido = ""
                                print("Se ha borrado el apellido.\n")
                                perfil.mostrar()
                                break

                    elif borrar == "3":
                        for perfil in info_usuarios:
                            if perfil.user == user_self.user:
                                perfil.correo = ""
                                print("Se ha borrado el correo.\n")
                                perfil.mostrar()
                                break
                            
                    elif borrar == "4":
                        for perfil in info_usuarios:
                            if perfil.user == user_self.user:
                                perfil.user = ""
                                print("Se ha borrado su username.\n")
                                perfil.mostrar()
                                break
                            
                    elif borrar == "5":
                        for perfil in info_usuarios:
                            if perfil.user == user_self.user:
                                if isinstance(perfil,Estudiante):
                                    perfil.carrera = ""
                                    print("\nSe ha borrado su carrera.\n")
                                    perfil.mostrar()
                                    break
                                elif isinstance(perfil,Profesor):
                                    perfil.departamento = ""
                                    print("\nSe ha borrado su departamento.\n")
                                    perfil.mostrar()
                                elif isinstance(perfil,Admin):
                                    print("Error. No puede borrar su especialidad.")
                                    perfil.mostrar()
                                break
                    
                    volver = input("\n¿Volver a borrar datos?: \n1- Si \n2- No \n==>")
                    if volver == "2":
                        break
                    
# #---------------------------------------------------------------------------------------------------------------------------------------------                
                
            elif opcion1 == "4":
                
                while True:
                    usua = input("\nIngrese el username: ")
                    coincidencias = False
                    for perfil in info_usuarios:
                        if perfil.user == usua:
                            coincidencias = True
                            print("\n")
                            perfil.solo_mostrar()
                            
                            if isinstance(user_self, Admin):
                                eliminar = input("\n¿Desea eliminar a este usuario? \n1- Si \n2- No \n>> ")
                                if eliminar == "1":
                                    info_usuarios.remove(usua)
                            
                            coincidencias = False
                            print("\nListado de publicaciones\n")
                            for post in info_publicaciones:
                                    n=1
                                    for i, post in enumerate(info_publicaciones):                                        
                                        if post.publisher == perfil.id_user:
                                            print("\n")
                                            print(f"({n})")
                                            post.mostrar__()
                                            n += 1
                                            
                                    selecc = input("\nSeleccione el post que desea ver >>> ")
                                    n = 1
                                    for post in info_publicaciones:
                                        if post.publisher == perfil.id_user:
                                            if n == int(selecc):
                                                print("\n")
                                                post.mostrar_publi()
                                                
                                                like = input("\n¿Quieres darle like al post? \n1- Si \n2- No \n>> ")
                                                if like == "1":
                                                    post.like.append(user_self.user)
                                                    print(f"Le gusta a {user_self.user}\n")

                                   
                                                
                                                comentario = input("¿Desea agregar un comentario?\n1- Si \n2- No \n>> ")
                                                if comentario == "2":
                                                    break
                                                if comentario == "1":
                                                    comment = input("\nEscriba su comentario: ")
                                                    print("\n")
                                                    post.comentario.append(comment)
                                                    post.mostrar_publi()
                                                    for comment in post.comentario:
                                                        print(f"\n-Comentarios:\n {user_self.user}: {comment}")
                                                    
     
                                                        
                                                        if isinstance(user_self, Admin):
                                                            eliminar = input("\n¿Desea eliminar un comentario? \n1- Si \n2- No \n>> ")
                                                            if eliminar == "1":
                                                                print("\n¿Cuál comentario desea borrar?")
                                                                for i, comentario in enumerate(post.comentario, 1):
                                                                    print(f"{i}. {comentario}")
                                                                    opcion = input("\nElige el comentario que desea borrar: ")
                                                                    post.comentario.pop(int(opcion)-1)
                                                                    print("Mensaje borrado.")
                                                    break
                                                
                                                
                                                if isinstance(user_self, Admin):
                                                    eliminar = input("\n¿Desea eliminar este post? \n1- Si \n2- No \n>> ")
                                                    if eliminar == "1":
                                                        print("¡Post eliminado!\n")
                                                        info_publicaciones.remove(post)
                                                    else:
                                                        break
                                            
                                                            
                                                        
                                                    break                                            
                                                
                                            else:
                                                n += 1
                                            
                                    seguir = input("\n¿Desea seguir esta cuenta? \n1- Si \n2- No \n==>")
                                    if seguir == "1":
                                        user_self.followers.append(perfil.id_user)
                                        break
                                    else:
                                        break
                        
            
                    volver = input("\n¿Desea acceder a otro usuario?: \n1- Si \n2- No \n==>")
                    if volver == "2":
                        break    
                        
                                                   
# ###################################################################################################################################################           
        elif menu == "2":
            post = input("\nSeleccione una opción: \n(1) Registrar datos del post \n(2) Ver post \n(3) Buscar post \n==>")
            
            if post == "1":
                         
                multimedia = input("·Ingrese el tipo de multimedia (foto/video): ") 
                descripcion = input("·Ingrese la descripción: ") 
                hashtag = input("·Ingrese el hashtag: ") 
                fecha = input("·Ingrese la fecha: ")
                url = input("·Ingrese url: ")
                
                for perfil in info_usuarios:
                    for post in info_publicaciones:
                        if post.publisher == perfil.id_user:
                            publicacion = Post(user_self.user, multimedia, descripcion, fecha, hashtag, {"type": multimedia , "url": url})
                            info_publicaciones.append(publicacion)
                   
# #-----------------------------------------------------------------------------------------------------------------------------------------------------                   
                    
            elif post == "2":
                
                for perfil in info_usuarios:
                    if isinstance(user_self, Profesor) and isinstance(perfil, Profesor):
                        if perfil.departamento == user_self.departamento:
                            print(f"\nSe ha agregado a {perfil.user} en tu lista de seguidores.")
                            user_self.followers.append(perfil.id_user)
                    elif isinstance(user_self, Estudiante) and isinstance(perfil, Estudiante):
                        if perfil.carrera == user_self.carrera:
                            print(f"\nSe ha agregado a {perfil.user} en tu lista de seguidores.")
                            user_self.followers.append(perfil.id_user)
                            
                
                while True:
                    ver = input("\n¿Qué usuario desea ver?: ")
                    for perfil in info_usuarios:
                        if perfil.user == ver:
                            print("\n")
                            perfil.mostrar()
                            
                            
                            if perfil.id_user in user_self.followers:
                                print("\nPublicaciones:")
                                for post in info_publicaciones:
                                        if post.publisher == perfil.id_user:
                                            print("\n")
                                            post.mostrar_publi()
                                            

                
                            else:
                                print("\nNo puedes ver la cuenta de este usuario porque no lo sigues.")
                                desear = input("\n¿Deseas seguir esta cuenta? \n1- Si \n2- No \n >>")
                                if desear == "1":
                                    user_self.followers.append(perfil.id_user)
                                                    
                                else:
                                    break                       
                        
                    
                    volver = input("\nVer a otro usuario: \n1- Si \n2- No \n==>")
                    if volver == "2":
                        break                  
# #-----------------------------------------------------------------------------------------------------------------------------------------------------                
            elif post == "3":
                while True:
                    opcion3 = input("\nElige de qué forma desea buscar. \n(1) Username \n(2) Hashtags\n==>")
                    
                    if opcion3 == "1":
                        username = input("Ingrese el username: ")
                        for perfil in info_usuarios:
                            if perfil.user == username:
                                print("\nSe ha encontrado al usuario\n")
                                break

                        if perfil.id_user in user_self.followers:
                            print("Estas son sus publicaciones:\n")
                            for post in info_publicaciones:
                                    if post.publisher == perfil.id_user:
                                        print("\n")
                                        post.mostrar_publi()
                            
                            
                        else:
                            print("No puedes ver la cuenta de este usuario porque no lo sigues.")
                            desear = input("\n¿Deseas seguir esta cuenta? \n1- Si \n2- No \n >>")
                            if desear == "1":
                                user_self.followers.append(perfil.id_user)
                                                
                            else:
                                break                                   
                        
                    
                    elif opcion3 == "2":
                        
                        hashtag = input("Ingrese los hashtag: ")                        
                        print("\nEstas son las publicaciones existentes con ese hashtag:")
                        for post in info_publicaciones:
                            for tag in post.hashtag:
                                if tag == hashtag:
                                    for user in info_usuarios:
                                        if user.id_user == post.publisher:
                                            usuario = user
                                    if usuario.id_user in user_self.followers:
                                        print("\n")
                                        post.mostrar_publi()
                                    else:
                                        print(f"Post de {usuario.user} (No sigues a este usuario)")
                    
                    
                    volver = input("\n¿Desea buscar de nuevo?: \n1- Si \n2- No \n==>")
                    if volver == "2":
                        break  

###################################################################################################################################################                   

main()