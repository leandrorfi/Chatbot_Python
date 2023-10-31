from flask import Flask, render_template, request, jsonify
import openai

# Configure a chave de API
chave_api = ""
openai.api_key = chave_api

# Inicialize o aplicativo Flask
app = Flask(__name__)

def enviar_mensagem(mensagem):
    script = "Somente mande a frase corrigida: " + mensagem
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": script},
        ],
        max_tokens=50  # Limita a resposta a 50 tokens
    )

    return resposta["choices"][0]["message"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_mensagem', methods=['POST'])
def processar_mensagem():
    mensagem = request.form['mensagem']
    resposta = enviar_mensagem(mensagem)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)