from flask import Flask, render_template, Response, send_from_directory
from tracker import Tracker

# Flask, and we specify our static files
app = Flask(__name__, static_url_path='/static')

# Index
@app.route('/')
def index():
    return render_template('index.html') # Renders template

# Generates image from webcam
def gen(t):
    while True:
        frame = t.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Video stream
@app.route('/video')
def video_feed():
    return Response(gen(Tracker()), mimetype='multipart/x-mixed-replace; boundary=frame')

# Images
@app.route('/img/<path:filename>')
def send_pic(filename):
    return send_from_directory('img', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False) # 0.0.0.0 so its open to all ports
