from ObjectDetector import Detector
import io
from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)
Scanner = Detector()


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def upload():
    if request.method == 'POST':
        file = Image.open(request.files['file'].stream)
        img = Scanner.detectObject(file)
        imgUP = send_file(io.BytesIO(img), attachment_filename='image.jpg', mimetype='image/jpg')
        return imgUP


if __name__ == "__main__":
    app.run()
