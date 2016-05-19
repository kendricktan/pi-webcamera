from flask import Flask, render_template, Response
from tracker import Tracker 

# Out tracker instance
tracker = Tracker()

# Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(t):
    while True:
        frame = t.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video')
def video_feed():
    return Response(gen(tracker), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
