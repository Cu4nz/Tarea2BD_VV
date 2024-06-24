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
                    "nombre" : nombre,
                    "correo" : email,
                    "clave" : clave ,
                    "descripcion" : desc
                    })
        print(respuesta.status_code)
        if respuesta.status_code == 200:
            respuesta_json = respuesta.json()
            print(f"Usuario registrado correctamente: {respuesta_json.get('mensaje')}")
            break
        elif respuesta.status_code==400:
            respuesta_json = respuesta.json()
            print(f"{respuesta_json.get('mensaje')}")
            

def bloquear():
    correo_usuario=input("Confirmar correo de sesión actual: ")
    clave_usuario=input("Confirmar clave: ")
    correo_bloq=input("Correo de usuario a bloquear: ")
    respuesta=requests.post("f{url}/bloquear", json={
        "correo" : correo_usuario,
        "clave" : clave_usuario,
        "correo_bloquear" : correo_bloq})
    
    if respuesta.status_code == 200:
        respuesta_json = respuesta.json()
        print(f"{respuesta_json.get('mensaje')}")
    elif respuesta.status_code==400:
        respuesta_json = respuesta.json()
        print(f"Datos del usuario: {respuesta_json.get('usuario')}")
        
            
    
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
        respuesta = requests.post(f"{url}/login",json={
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
    respuesta=requests.post(f"{url}/enviarcorreo",json={
        "correo" : correo_destino,
        "mensaje" : mensaje
        })
    
    

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
    print("1. Enviar correo: ")
    print("2. Ver informaci´on de una direcci´on de correo electrónico ")
    print("3. Bloquear a usuario: ")
    print("4. Ver correos favoritos ")
    print("5. Marcar correo como favorito ")
    print("6. Desmarcar correo como favorito ")
    print("7. Cerrar sesión")
    

if __name__ == "__main__":
    main()
    
            

            
        
        
    
