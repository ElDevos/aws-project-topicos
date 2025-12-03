# AWS Project - Tópicos

Este proyecto consiste en una aplicación web completa (Frontend + Backend + Base de Datos) lista para ser desplegada en AWS, pero configurada para pruebas locales sencillas usando Docker.

## 📂 Estructura del Proyecto

- **BACKEND/**: API en Python (Flask) que maneja la lógica y conexión a base de datos.
- **FRONTEND/**: Aplicación Web (Flask + HTML) que consume la API.
- **docker-compose.yml**: Configuración para levantar la base de datos MySQL localmente.

## 🚀 Requisitos Previos

1.  **Python 3.10+** instalado.
2.  **Docker Desktop** instalado y ejecutándose.

## 🛠️ Configuración Inicial

### 1. Base de Datos (Docker)
Para iniciar la base de datos MySQL localmente, abre una terminal en la carpeta raíz del proyecto y ejecuta:

```bash
docker-compose up -d db
```

Esto levantará un contenedor MySQL en el puerto `3306`.
*Nota: Espera unos segundos la primera vez para que la base de datos se inicialice completamente.*

### 2. Entorno Virtual (Opcional pero recomendado)
Crea y activa un entorno virtual para instalar las dependencias:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
Instala las librerías necesarias para el Backend y Frontend:

```bash
pip install -r BACKEND/requirements.txt
pip install requests  # Necesario para el Frontend
```

## ▶️ Ejecución

Necesitarás **dos terminales** abiertas (una para el Backend y otra para el Frontend).

### Terminal 1: Backend
```bash
python BACKEND/app.py
```
*Debería indicar que está corriendo en el puerto 5000 y que la base de datos se inicializó correctamente.*

### Terminal 2: Frontend
```bash
python FRONTEND/app.py
```
*Debería indicar que está corriendo en el puerto 3000.*

## 🌐 Probar la Aplicación

Abre tu navegador y ve a:
👉 **http://127.0.0.1:3000**

Desde allí podrás:
1.  Ver la lista de usuarios y productos.
2.  **Crear** nuevos registros.
3.  **Editar** registros existentes.
4.  **Eliminar** registros.

## ☁️ Despliegue en AWS (Futuro)

Este proyecto está diseñado para AWS. Para desplegarlo:
1.  **Base de Datos**: Crea una instancia RDS (MySQL).
2.  **Configuración**: Actualiza las variables de entorno en tu servicio (ECS/Lambda) con los datos de tu RDS (Host, Usuario, Contraseña).
    *   No necesitas cambiar el código, solo las variables de entorno.
