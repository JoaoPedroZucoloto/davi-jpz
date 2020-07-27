import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def nao_entre_em_panico():
    with open('caminho-completo/teste.txt', 'a') as file:
            file.write(request.data.decode('utf-8'))
            file.read()

@app.route("/webhook", methods=['GET','POST'])
def webhook_handle():
    ar = 'Lente Azul'
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    if challenge != '*' and verify_token == 'chupacabra':
        return challenge

    output = request.get_json()
    return output

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
