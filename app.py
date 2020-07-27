import os
from flask import Flask, jsonify, request

app = Flask(__name__)
WP_API_URL   = 'https://graph.facebook.com/v2.6/me/messages?access_token=TEU-TOKEN-AQUI'

@app.route("/webhook", methods=['GET'])
def webhook_handle():
    challenge       = request.args.get('hub.challenge',    default = '*', type = str)
    verify_token    = request.args.get('hub.verify_token', default = '',  type = str)
    if challenge != '*' and verify_token == 'chupacabra':
        return challenge

    #data = request.data.decode('utf-8')
    data = json.loads(request.data.decode('utf-8'))
    return jsonify(data)


def send_message(recipient_id, text): 
    response = requests.post(WP_API_URL, headers=WP_HEADER, data=json.dumps({
        'recipient' : {'id'   : recipient_id},
        'message'   : {'text' : text}
    }))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
