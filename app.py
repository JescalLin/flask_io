from flask import Flask, config, render_template
from flask import Flask, make_response, request, Response
from flask_socketio import SocketIO, send  
from flask import redirect, url_for
from urllib.request import urlopen


#初始化
app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

def ack():
    print('message was received')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send')
def chat(data):
    socketio.emit('get', data, callback=ack())

@socketio.on('test')
def test():
    socketio.send("test", callback=ack())

@socketio.on('image')
def img(image):
    img = image['file']
    
    with urlopen(img) as response:
        data = response.read()
    #print(data.decode('base64'))
    # with open("image.png", "wb") as f:
    #     f.write(data)
    # print(image['fileName'])
    
    socketio.emit('get_image', img, callback=ack())

if __name__ == '__main__':
    app.run()

