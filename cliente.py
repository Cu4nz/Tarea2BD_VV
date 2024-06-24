import requests

url="algo.cl"

def registrar():
    while True:
        nombre=input("Ingrese nombre de usuario: ")
        email=input("Ingrese correo electónico: ")
        clave=input("Ingrese clave: ")
        desc=input("Ingrese una descripción del perfil: ")
        
        #Cambiar url acorde, probar
        respuesta = requests.post(f"{url}/registrar", json={
                    "nombre" : nombre,
                    "correo" : email,
                    "clave" : clave ,
                    "descripcion" : desc
                    })
        
        #Recordar usuario o email repetido

def bloquear():
    correo_usuario=input("Confirmar correo de sesión actual: ")
    clave_usuario=input("Confirmar clave: ")
    correo_bloq=input("Correo de usuario a bloquear: ")
    respuesta=requests.post("f{url}/bloquear", json={
        "correo" : correo_usuario,
        "clave" : clave_usuario,
        "correo_bloquear" : correo_bloq})
    
def ver_usuario():
    correo_ver=input("Ingrese el correo del usuario a ver: ")
    respuesta=requests.get(f"{url}/informacion/:correo",json={
        "correo" : correo_ver
        })

def marcar_favorito():
    correo_fav=input("Ingrese correo: ")
    clave_fav=input("Ingrese clave: ")
    id_correo=input("Ingrese la id del correo: ")
    respuesta=requests.post(f"{url}/marcarcorreo", json={
        "correo" : correo_fav,
        "clave" : clave_fav,
        "id_correo_favorito" : id_correo
        })

def desmarcar_favorito():
    correo_del=input("Ingrese correo: ")
    clave_del=input("Ingrese clave: ")
    id_correo=input("Ingrese la id del correo: ")
    respuesta=requests.delete(f"{url}/desmarcarcorreo", json={
        "correo" : correo_del,
        "clave" : clave_del,
        "id_correo_favorito" : id_correo
        })
    

    
        
def ingresar():
    while True:
        correo=input("Ingrese correo electrónico: ")
        clave=input("Ingrese clave: ")
        respuesta = requests.post(f"{url}/register",json={
            "correo" : correo,
            "clave" : clave
            })
        if respuesta==1:
            print("Correo no existe, intente nuevamente.")
        elif respuesta==2:
            print("Clave incorrecta")
        else:
            menu()
def enviar():
    correo_destino=input("Ingrese correo del destinatario: ")
    mensaje=input("Ingrese mensaje a enviar: ")


    
    
def main():
    while True:
        print("Bienvenido")
        print("1. Ingresar \n 2. Registrarse \n 3. Salir")
        op=int(input("Seleccione la opcion que desee: "))
        if op==1:
            ingresar()
        elif op==2:
            registrar()
        elif op==3:
            break
        else:
            print("Opción inválida, seleccione nuevamente")

def menu():
    print("Menú \n")
    print("1. Enviar correo: \n")
    print("2. Ver informaci´on de una direcci´on de correo electrónico \n")
    print("3. Ver correos favoritos \n")
    print("4. Marcar correo como favorito \n")
    print("5. Cerrar sesión")
    
    
    
            

            
        
        
    
