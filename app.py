import os
import sys  # Adicione esta linha
from pymongo import MongoClient
from flask import Flask

# Verifique se a variável de ambiente 'MONGO_URI' está definida
mongo_uri = os.getenv('MONGO_URI')
if mongo_uri is None:
    print("Erro: A variável de ambiente 'MONGO_URI' não está definida.")
    sys.exit(1)  # Encerra a aplicação caso não tenha a URI do MongoDB

client = MongoClient(mongo_uri)  # Conexão com o MongoDB

# Criando a aplicação Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    # Rodando a aplicação com Gunicorn
    app.run(host='0.0.0.0', port=5000)
