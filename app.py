from flask import Flask, request, render_template, redirect, url_for, send_file
from threading import Thread
import csv
from datetime import datetime
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

now = datetime.today().strftime('%d-%m-%Y')
bot = telegram.Bot(token=os.environ['TOKEN'])

def send(text):
      print("sendou")
      #telegram_send.send(messages=[text], parse_mode= 'Markdown')
      bot.sendMessage(chat_id=-4194652894, text=text, parse_mode= 'Markdown')
      #telegram_send.send(messages=[text], parse_mode= 'Markdown')

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/get_data', methods=['POST'])
def get_data():
  nome = request.form.get('nome')
  telefone = request.form.get('telefone')
  pedido = request.form.get('mensagem')
  phone = request.form.get('phone')
  text = request.form.get('text')

  msg = """
## Novo contato
:bulb: Alguém precisa de Esperença :bulb: :pray:

:clipboard: **Nome:"""+str(nome)+"""**  
:iphone: **Telefone:"""+str(telefone)+"""**  
:pray: **Pedido de Oração:"""+str(pedido)+"""** 
"""
  
  #send telegram message
  send(msg)

  # with open('dados.csv', 'a', newline='') as arquivo_csv:
  #   writer = csv.writer(arquivo_csv)
  #   dados = [
  #     nome, telefone, pedido
  #   ]
  #   writer.writerow(dados)
  
  return redirect("https://api.whatsapp.com/send?phone=" + str(phone) +
                  "&text=" + str(text) + "&mensagem=" + str(pedido))


@app.route('/live')
def home():
  return 'I am Alive in ' + str(now)


