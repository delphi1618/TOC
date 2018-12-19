import os
from bottle import Bottle, request, abort, static_file, route, run
from utils import send_text_message
from fsm import TocMachine

app = Bottle()

VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']

machine = TocMachine(
    states=[
        'user',
        'start1',
        'music1',
        'music2',
        'ch1',
        'ch2',
        'ch3',
        'jp1',
        'jp2',
        'jp3',
        'fun1',
        'fun2',
        'fun3',
        'fun4',
        'joke1',
        'joke2',
        'joke3',
        'joke4',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'start1',
            'conditions': 'to_start1'
        },
        {
            'trigger': 'advance',
            'source': 'start1',
            'dest': 'music1',
            'conditions': 'to_music1'
        },
        {
            'trigger': 'advance',
            'source': 'start1',
            'dest': 'fun1',
            'conditions': 'to_fun1'
        },
        {
            'trigger': 'advance',
            'source': 'start1',
            'dest': 'joke1',
            'conditions': 'to_joke1'
        },
        {
            'trigger': 'advance',
            'source': 'music1',
            'dest': 'music2',
            'conditions': 'to_music2'
        },
        {
            'trigger': 'advance',
            'source': 'music2',
            'dest': 'jp1',
            'conditions': 'to_jp1'
        },
        {
            'trigger': 'advance',
            'source': 'jpl',
            'dest': 'jp2',
            'conditions': 'to_jp2'
        },
        {
            'trigger': 'advance',
            'source': 'jp2',
            'dest': 'jp3',
            'conditions': 'to_jp3'
        },
        {
            'trigger': 'advance',
            'source': 'music2',
            'dest': 'ch1',
            'conditions': 'to_ch1'
        },
        {
            'trigger': 'advance',
            'source': 'chl',
            'dest': 'ch2',
            'conditions': 'to_ch2'
        },
        {
            'trigger': 'advance',
            'source': 'ch2',
            'dest': 'ch3',
            'conditions': 'to_ch3'
        },
        {
            'trigger': 'advance',
            'source': 'fun1',
            'dest': 'fun2',
            'conditions': 'to_fun2'
        },
        {
            'trigger': 'advance',
            'source': 'fun2',
            'dest': 'fun3',
            'conditions': 'to_fun3'
        },
        {
            'trigger': 'advance',
            'source': 'fun3',
            'dest': 'fun4',
            'conditions': 'to_fun4'
        },
        {
            'trigger': 'advance',
            'source': 'joke1',
            'dest': 'joke2',
            'conditions': 'to_joke2'
        },
        {
            'trigger': 'advance',
            'source': 'joke2',
            'dest': 'joke3',
            'conditions': 'to_joke3'
        },
        {
            'trigger': 'advance',
            'source': 'joke3',
            'dest': 'joke4',
            'conditions': 'to_joke4'
        },
        {
            'trigger': 'go_back',
            'source': [
                'jp3',
                'ch3',
                'joke4',
                'fun4',
            ],
            'dest': 'start1'
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
        machine.advance(event)
        return 'OK'


		
@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')
		

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
