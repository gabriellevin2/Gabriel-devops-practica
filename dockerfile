# 1. Imagen base
FROM python:3.12-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar dependencias primero (para aprovechar la cache)
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente
COPY . .

# 7. Comando de inicio
# Ajusta la ruta si tu main está en otro sitio
CMD ["python","main.py"]