from flask import Flask, render_template,url_for,send_file,make_response,request,redirect,send_from_directory

app = Flask(__name__)

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
    resp = make_response(render_template('index.html'),200)
    return resp

@app.route('/gen_evidance',methods=["POST","GET"])
def image():
    data = request.get_json()
    print(data)
    resp = make_response(render_template('index.html'),200)
    return resp



app.run('0.0.0.0',8080)