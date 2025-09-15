from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Récupération des variables d'environnement
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))

# Connexion à MongoDB
client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = client["testdb"]  # base de données
collection = db["messages"]  # collection


@app.route('/')
def hello_world():
    # Insérer un message dans la base
    collection.insert_one({"message": "Hello, MongoDB!"})
    count = collection.count_documents({})
    return f'Hello, World! Messages count: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)