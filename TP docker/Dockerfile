# Utiliser une image Python officielle comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier uniquement app.py dans le conteneur
COPY app.py .

# Installer Flask
RUN pip install --no-cache-dir flask

# Exposer le port 5000
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
