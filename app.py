import time
from flask import Flask, render_template, request, redirect, url_for
import webbrowser
import ocrGoogleCloud


app = Flask(__name__)
webbrowser.open("http://127.0.0.1:5000")
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clicked')
def clicked():
    path = ocrGoogleCloud.OCR().capture_image()
    t = ocrGoogleCloud.OCR().detect_text(path=path)
    t = str(t)
    t += "saurin"
    time.sleep(2)
    return render_template('clicked.html', something=t)

app.run(debug=True)
