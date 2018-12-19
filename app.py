import os
from bottle import Bottle, request, abort, static_file, route, run
from utils import send_text_message
from fsm import TocMachine

app = Bottle()

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
#VERIFY_TOKEN = '1234'
PORT = os.environ['PORT']
#PORT = '12345'

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


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
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
		if event.get("message"):
            text = 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Tokyo_Metropolitan_Government_Building_2012.JPG'
            sender_id = event['sender']['id']
            send_text_message(sender_id, text)
        machine.advance(event)
        return 'OK'

@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
