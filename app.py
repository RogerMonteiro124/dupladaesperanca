from flask import Flask, request, render_template, redirect, url_for, send_file
from threading import Thread
import csv
from datetime import datetime

now = datetime.today().strftime('%d-%m-%Y')

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

  with open('dados.csv', 'a', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    dados = [
      nome, telefone, pedido
    ]
    writer.writerow(dados)
  
  return redirect("https://api.whatsapp.com/send?phone=" + str(phone) +
                  "&text=" + str(text) + "&mensagem=" + str(pedido))


@app.route('/live')
def home():
  return 'I am Alive in ' + str(now)

def run():
  app.run(host='0.0.0.0', port=10000)

run()
