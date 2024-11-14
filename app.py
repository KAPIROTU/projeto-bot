from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Aplicação rodando!', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Processar dados do webhook aqui
    return jsonify({'status': 'received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
