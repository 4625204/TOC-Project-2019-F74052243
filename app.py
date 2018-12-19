from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = "sunsun"
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11',
        'state12',
        'state21',
        'state22',
        'state31',
        'state32',
        'state41',
        'state42',
        'state51',
        'state52',
        'state61',
        'state62',
        'state71',
        'state72',
        'state81',
        'state82',
        'state91',
        'state92',
        'state101',
        'state102',
        'stateback',
        'stateimg1',
        'stateimg2',
        'stateimg3',
        'stateimg4',
        'stateimg5',
        'stateimg6',
        'stateimg7',
        'stateimg8',
        'stateimg9',
        'stateimg10'
        
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
            'source': ['state1','state12','stateimg1'],
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': ['state1','state11','stateimg1'],
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger':'advance',
            'source':['state1','state11','state12'],
            'dest':'stateimg1',
            'conditions': 'is_going_to_stateimg1'
        },
        
        
        
        
        
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': ['state2','state22','stateimg2'],
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': ['state2','state21','stateimg2'],
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
        {
            'trigger':'advance',
            'source':['state2','state21','state22'],
            'dest':'stateimg2',
            'conditions': 'is_going_to_stateimg2'
        },
        



        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': ['state3','state32','stateimg3'],
            'dest': 'state31',
            'conditions': 'is_going_to_state31'
        },
        {
            'trigger': 'advance',
            'source': ['state3','state31','stateimg3'],
            'dest': 'state32',
            'conditions': 'is_going_to_state32'
        },
        {
            'trigger':'advance',
            'source':['state3','state31','state32'],
            'dest':'stateimg3',
            'conditions': 'is_going_to_stateimg3'
        },
        



        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': ['state4','state42','stateimg4'],
            'dest': 'state41',
            'conditions': 'is_going_to_state41'
        },
        {
            'trigger': 'advance',
            'source': ['state4','state41','stateimg4'],
            'dest': 'state42',
            'conditions': 'is_going_to_state42'
        },
        {
            'trigger':'advance',
            'source':['state4','state41','state42'],
            'dest':'stateimg4',
            'conditions': 'is_going_to_stateimg4'
        },
        
        

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': ['state5','state52','stateimg5'],
            'dest': 'state51',
            'conditions': 'is_going_to_state51'
        },
        {
            'trigger': 'advance',
            'source': ['state5','state51','stateimg5'],
            'dest': 'state52',
            'conditions': 'is_going_to_state52'
        },
        {
            'trigger':'advance',
            'source':['state5','state51','state52'],
            'dest':'stateimg5',
            'conditions': 'is_going_to_stateimg5'
        },
        




         {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
       {
            'trigger': 'advance',
            'source': ['state6','state62','stateimg6'],
            'dest': 'state61',
            'conditions': 'is_going_to_state61'
        },
        {
            'trigger': 'advance',
            'source': ['state6','state61','stateimg6'],
            'dest': 'state62',
            'conditions': 'is_going_to_state62'
        },
        {
            'trigger':'advance',
            'source':['state6','state61','state62'],
            'dest':'stateimg6',
            'conditions': 'is_going_to_stateimg6'
        },



        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': ['state7','state72','stateimg7'],
            'dest': 'state71',
            'conditions': 'is_going_to_state71'
        },
        {
            'trigger': 'advance',
            'source': ['state7','state71','stateimg7'],
            'dest': 'state72',
            'conditions': 'is_going_to_state72'
        },
        {
            'trigger':'advance',
            'source':['state7','state71','state72'],
            'dest':'stateimg7',
            'conditions': 'is_going_to_stateimg7'
        },
        


        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
       {
            'trigger': 'advance',
            'source': ['state8','state82','stateimg8'],
            'dest': 'state81',
            'conditions': 'is_going_to_state81'
        },
        {
            'trigger': 'advance',
            'source': ['state8','state81','stateimg8'],
            'dest': 'state82',
            'conditions': 'is_going_to_state82'
        },
        {
            'trigger':'advance',
            'source':['state8','state81','state82'],
            'dest':'stateimg8',
            'conditions': 'is_going_to_stateimg8'
        },
        


        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
       {
            'trigger': 'advance',
            'source': ['state9','state92','stateimg9'],
            'dest': 'state91',
            'conditions': 'is_going_to_state91'
        },
        {
            'trigger': 'advance',
            'source': ['state9','state91','stateimg9'],
            'dest': 'state92',
            'conditions': 'is_going_to_state92'
        },
        {
            'trigger':'advance',
            'source':['state9','state91','state92'],
            'dest':'stateimg9',
            'conditions': 'is_going_to_stateimg9'
        },




        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': ['state10','state102','stateimg10'],
            'dest': 'state101',
            'conditions': 'is_going_to_state101'
        },
        {
            'trigger': 'advance',
            'source': ['state10','state101','stateimg10'],
            'dest': 'state102',
            'conditions': 'is_going_to_state102'
        },
        {
            'trigger':'advance',
            'source':['state10','state101','state102'],
            'dest':'stateimg10',
            'conditions': 'is_going_to_stateimg10'
        },
        
        {
            'trigger': 'advance',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6',
                'state7',
                'state8',
                'state9',
                'state10',
                'state11',
                'state21',
                'state31',
                'state41',
                'state51',
                'state61',
                'state71',
                'state81',
                'state91',
                'state101',
                'state12',
                'state22',
                'state32',
                'state42',
                'state52',
                'state62',
                'state72',
                'state82',
                'state92',
                'state102',
                'stateimg1',
                'stateimg2',
                'stateimg3',
                'stateimg4',
                'stateimg5',
                'stateimg6',
                'stateimg7',
                'stateimg8',
                'stateimg9',
                'stateimg10',
            ],
            'dest': 'stateback',
            'conditions': 'is_going_to_stateback'
        },
        
        {
            'trigger': 'go_back',
            'source': 'stateback',
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
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
    run(host="localhost", port=5000, debug=True)
    show_fsm()