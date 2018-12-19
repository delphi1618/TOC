import os
from bottle import Bottle, request, abort, static_file
from utils import send_text_message

app = Bottle()

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

@app.route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)

@app.route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if event.get("message"):
            text = 'text'
            sender_id = event['sender']['id']
            send_text_message(sender_id, text)
        return 'OK'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
