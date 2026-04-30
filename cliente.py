import requests
import sys

URL_BASE = "http://127.0.0.1:5000"

def registrar_usuario():
    print("\n--- REGISTRO ---")
    usuario = input("Ingresa un nombre de usuario: ")
    contrasena = input("Ingresa una contraseña: ")
    
    payload = {"usuario": usuario, "contraseña": contrasena}
    respuesta = requests.post(f"{URL_BASE}/registro", json=payload)
    
    print(f"Respuesta del servidor ({respuesta.status_code}):", respuesta.json())

def iniciar_sesion():
    print("\n--- LOGIN ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    payload = {"usuario": usuario, "contraseña": contrasena}
    respuesta = requests.post(f"{URL_BASE}/login", json=payload)
    
    print(f"Respuesta del servidor ({respuesta.status_code}):", respuesta.json())
    
    # Si el login es exitoso ---> (código 200), hacemos la petición a /tareas
    if respuesta.status_code == 200:
        print("\n[!] Accediendo al panel de tareas...")
        respuesta_tareas = requests.get(f"{URL_BASE}/tareas")
        print("\n--- CONTENIDO DE /tareas (HTML) ---")
        print(respuesta_tareas.text)
        print("-----------------------------------")

def mostrar_menu():
    while True:
        print("\n=== SISTEMA DE TAREAS ===")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            print("Saliendo del cliente...")
            sys.exit()
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == '__main__':
    try:
        # Verifico si el servidor está corriendo antes de abrir el menú
        requests.get(URL_BASE)
        mostrar_menu()
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar a la API.")