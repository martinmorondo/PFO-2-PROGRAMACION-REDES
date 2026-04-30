# PFO 2: Programación de Redes - Sistema de Gestión de Tareas

Este proyecto es la resolución del Trabajo Práctico Final (PFO 2) de Programación de Redes. Consiste en el desarrollo de una API REST utilizando **Flask** y **SQLite**, que permite la gestión de usuarios mediante autenticación básica, contraseñas seguras (hasheadas) y la visualización de un panel de tareas.

## 🚀 Requisitos Previos

Asegúrate de tener instalado Python 3.x en tu sistema. Además, necesitarás instalar las siguientes dependencias:

```bash
pip install flask werkzeug requests

##  Respuestas Conceptuales

### 1. ¿Por qué hashear contraseñas?
Hashear las contraseñas es una práctica de seguridad esencial. A diferencia del cifrado simétrico, el hashing es una función unidireccional; esto significa que una vez que la contraseña se transforma en un hash, no se puede "des-cifrar" para obtener el texto original. 
Esto protege a los usuarios en caso de que la base de datos sea vulnerada: un atacante solo vería cadenas de caracteres ilegibles, evitando el robo de credenciales y protegiendo la privacidad.

### 2. Ventajas de usar SQLite en este proyecto
Para este desarrollo, SQLite ofrece beneficios clave:
- **Portabilidad:** La base de datos es un simple archivo `.db`, lo que facilita mover el proyecto entre diferentes entornos sin configurar servidores externos.
- **Simplicidad:** No requiere un proceso de servidor independiente, lo que reduce la complejidad técnica y el consumo de recursos.
- **Integración nativa:** Se maneja directamente con la librería estándar de Python, lo que agiliza el desarrollo y asegura la compatibilidad.
