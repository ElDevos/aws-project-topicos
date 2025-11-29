FROM python:3.12-slim

WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# Exponer el puerto
EXPOSE 8080

# Definir variable de entorno para Flask
ENV FLASK_APP=main.py

# Comando para ejecutar la API
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]