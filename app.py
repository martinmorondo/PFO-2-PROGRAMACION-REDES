from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
DB_NAME = "sistema_tareas.db"

# Inicializar base de datos SQLite
def inicializar_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Endpoint 1: Registro de Usuarios
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({"error": "Faltan datos (usuario o contraseña)"}), 400
        
    usuario = datos['usuario']
    contrasena_plana = datos['contraseña']
    
    # Hasheamos la contraseña antes de guardarla
    contrasena_hasheada = generate_password_hash(contrasena_plana)
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", 
            (usuario, contrasena_hasheada)
        )
        conn.commit()
        conn.close()
        return jsonify({"mensaje": f"Usuario '{usuario}' registrado exitosamente."}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El nombre de usuario ya existe."}), 409

# Endpoint 2: Inicio de Sesión
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({"error": "Faltan credenciales"}), 400
        
    usuario = datos['usuario']
    contrasena_plana = datos['contraseña']
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conn.close()
    
    # Verificamos si el usuario existe y si el hash coincide con la contraseña ingresada
    if resultado and check_password_hash(resultado[0], contrasena_plana):
        return jsonify({"mensaje": "Inicio de sesión exitoso. Tienes acceso a las tareas."}), 200
    else:
        return jsonify({"error": "Credenciales inválidas."}), 401

# Endpoint 3: Gestión de Tareas (HTML de bienvenida)
@app.route('/tareas', methods=['GET'])
def tareas():
    # Retornamos un HTML básico
    html_bienvenida = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gestión de Tareas</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #2C3E50; }
            p { color: #34495E; }
        </style>
    </head>
    <body>
        <h1>¡Bienvenido al Sistema de Gestión de Tareas!</h1>
        <p>Tu inicio de sesión ha sido verificado. Aquí se mostrarán tus tareas en el futuro.</p>
    </body>
    </html>
    """
    return html_bienvenida, 200

if __name__ == '__main__':
    inicializar_db()
    # Ejecutamos el servidor en puerto 5000
    app.run(debug=True, port=5000)