from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Configuração da conexão com o MongoDB Atlas
# Usando o nome da variável de ambiente que você já está utilizando (exemplo: MONGO_URI)
client = MongoClient(os.getenv('MONGO_URI'))  # Substitua 'MONGO_URI' pelo nome correto da sua chave de ambiente
db = client.get_database()  # Acessa o banco de dados

# Testando a conexão com o MongoDB
@app.before_first_request
def test_db_connection():
    try:
        # Tentando acessar uma coleção simples
        db.list_collection_names()  # Verifica se conseguimos acessar o banco de dados
        print("Conexão com o MongoDB Atlas bem-sucedida!")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

@app.route('/')
def home():
    return 'Aplicação rodando!', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Processar dados do webhook aqui e, se necessário, gravar no MongoDB
    return jsonify({'status': 'received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
