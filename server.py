from flask import Flask, render_template,url_for,send_file,make_response,request,redirect,send_from_directory
from flask_socketio import SocketIO, send, rooms, emit, join_room, close_room, leave_room
import databaseutils
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_orgins="*")

#socket functions 
##########################################
@socketio.on('join')
def on_join(data):
    room = data['lobby']
    join_room(room)
    emit( 'my response',{'msg':room}, to=room)

@socketio.on('inital_prompt')
def initial_prompt(data):
    room = data['lobby']
    join_room(room)
    #load in the prompt
    emit( 'my response',{'msg':'story prompt'}, to=room)

@socketio.on('ready')
def ready(data):
    room = data['lobby']
    join_room(room)
    #set user to ready -> send back the status of ready so the box changes
    emit( 'my response',{'msg':room}, to=room)
    
@socketio.on('game_start')
def game_start(data):
    room = data['lobby']
    join_room(room)
    #set user to ready -> send back the status of ready so the box changes
    emit( 'my response',{'msg':room}, to=room)

@socketio.on('end_round')
def end_round(data):
    room = data['lobby']
    join_room(room)
    #set user to ready -> send back the status of ready so the box changes
    emit( 'my response',{'msg':room}, to=room)


#Flask Helper functions and routes
#------------------------
@app.route('/<path:path>')
def send_static(path):
    response = make_response(send_from_directory('static', path), 200)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response
#------------------------



@app.route('/')
def index():
    id = request.cookies.get('lobby',None)
    if id != None:
        lobby = databaseutils.get_lobby(id)
        if lobby != None:
            return redirect('/game')
    resp = make_response(render_template('index.html'),200)
    resp.set_cookie('lobby','1',max_age=0)
    resp.set_cookie('player','1',max_age=0)
    return resp

@app.route('/gen_evidance',methods=["POST","GET"])
def image():
    data = request.get_json()
    print(data)
    resp = make_response(render_template('index.html'),200)
    return resp

#-------------------------------
#Lobby routes


@app.route('/make_lobby',methods=['GET'])
def make_game():
   id = databaseutils.make_lobby()
   response = make_response(render_template('game.html'),200)
   response.set_cookie('lobby',id,3600)
   response.set_cookie('player','1')
   return response


@app.route('/join_code',methods=['POST'])
def join_game():
    cookie = request.cookies.get('lobby',None)
    lobby = request.form.get('code')
    print(lobby)
    joined = databaseutils.join_lobby(lobby)
    if joined:
        resp = make_response(redirect('/game'),301)
        resp.set_cookie('lobby',lobby,3600)
        return resp
    else:
        resp = make_response(redirect('/'),301)
        resp.set_cookie('lobby','N',0)
        return resp



#-------------------------------
#Game routes

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/card')
def card():
    return render_template('cards.html')


#-------------------------------
# Run the application

#app.run('0.0.0.0',8080)
socketio.run(app=app, host='0.0.0.0', port=8080, allow_unsafe_werkzeug=True)