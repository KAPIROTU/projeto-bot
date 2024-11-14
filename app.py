import os
from flask import Flask, request, jsonify
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, filters

app = Flask(__name__)

# Inicializar o bot com o token da variável de ambiente
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')  # Agora você usa a variável de ambiente corretamente
if not TELEGRAM_TOKEN:
    raise ValueError("Token do Telegram não encontrado. Configure a variável de ambiente TELEGRAM_TOKEN.")

bot = Bot(token=TELEGRAM_TOKEN)

# Funções para comandos do bot
def start(update, context):
    update.message.reply_text("Olá! Eu sou seu bot. Como posso ajudar?")

def echo(update, context):
    # Responde com a mesma mensagem que o usuário enviou
    update.message.reply_text(update.message.text)

# Configurar o Dispatcher para lidar com os comandos e mensagens
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Rota principal de verificação
@app.route('/')
def home():
    return 'Aplicação rodando!', 200

# Rota para o webhook do bot
@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    data = request.get_json()
    if data:
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)
    return jsonify({'status': 'received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
