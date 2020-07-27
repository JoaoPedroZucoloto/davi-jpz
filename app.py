import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():    
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    if challenge != '*' and verify_token == 'chupacabra':
        return challenge
       
    data = request.data.decode('utf-8')
        
    return 'Oi :)'


if __name__ == "__main__":
    app.run()
