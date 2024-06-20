import requests

def registrar():
    while True:
        nombre=input("Ingrese nombre de usuario: ")
        email=input("Ingrese correo electónico: ")
        clave=input("Ingrese clave: ")
        desc=input("Ingrese una descripción del perfil: ")
        
        #Recordar usuario o email repetido
        
def ingresar():
    print("por mientras")
    
        
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
            
    
            

            
        
        
    