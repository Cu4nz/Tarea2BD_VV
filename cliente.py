import requests

url="http://localhost:3000/api"

def registrar():
    while True:
        nombre=input("Ingrese nombre de usuario: ")
        email=input("Ingrese correo electónico: ")
        clave=input("Ingrese clave: ")
        desc=input("Ingrese una descripción del perfil: ")
        
        #Cambiar url acorde, probar
        respuesta = requests.post(f"{url}/registrar", json={
                    'nombre':nombre,
                    'correo':email,
                    'clave':clave ,
                    'descripcion':desc
                    })
        respuesta_json = respuesta.json()
        codigo=respuesta_json.get('estado')
        if codigo == 200:
            respuesta_json = respuesta.json()
            print(f"Usuario registrado correctamente: {respuesta_json.get('mensaje')}")
            break
        elif codigo==400:
            print(f"{respuesta_json.get('mensaje')}")
            

def bloquear():
    while True:
        correo_usuario=input("Confirmar correo de sesión actual: ")
        clave_usuario=input("Confirmar clave: ")
        correo_bloq=input("Correo de usuario a bloquear: ")
        respuesta=requests.post("f{url}/bloquear", json={
            "correo" : correo_usuario,
            "clave" : clave_usuario,
            "correo_bloquear" : correo_bloq})
        
        respuesta_json = respuesta.json()
        codigo=respuesta_json.get('estado')
        
        if codigo == 200:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
            break
        elif codigo == 400:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
        
            
    
def ver_usuario():
    while True:
        correo_ver=input("Ingrese el correo del usuario a ver: ")
        respuesta=requests.get(f"{url}/informacion/:correo",json={
            "correo" : correo_ver
            })
        respuesta_json = respuesta.json()
        codigo=respuesta_json.get('estado')
        if codigo == 200:
            respuesta_json = respuesta.json()
            print(respuesta_json.get)
            break
        elif codigo == 404:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
        elif codigo == 404:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))

def marcar_favorito():
    while True:
        
        correo_fav=input("Ingrese correo: ")
        clave_fav=input("Ingrese clave: ")
        id_correo=input("Ingrese la id del correo: ")
        respuesta=requests.post(f"{url}/marcarcorreo", json={
            "correo" : correo_fav,
            "clave" : clave_fav,
            "id_correo_favorito" : id_correo
            })
        respuesta_json = respuesta.json()
        codigo=respuesta_json.get('estado')
        if codigo== 200:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
            break
        if codigo == 404:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))


        
def ingresar():
    while True:
        correo=input("Ingrese correo electrónico: ")
        clave=input("Ingrese clave: ")
        respuesta = requests.post(f"{url}/login",json={
            "correo" : correo,
            "clave" : clave
            })
        respuesta_json = respuesta.json()
        codigo=respuesta_json.get('estado')
        if codigo==200:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
            menu()
        elif codigo==400:
            respuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
        elif codigo==404:
            prespuesta_json = respuesta.json()
            print(respuesta_json.get('mensaje'))
            


def main():
    while True:
        print("Bienvenido")
        print("1. Ingresar \n2. Registrarse \n3. Salir")
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
    print("1. Ver informaci´on de una direcci´on de correo electrónico ")
    print("2. Bloquear a usuario: ")
    print("3. Ver correos favoritos ")
    print("4. Marcar correo como favorito ")
    print("5. Cerrar sesión")
    

if __name__ == "__main__":
    main()
    
            

            
        
        
    
