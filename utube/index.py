from flask import Flask, url_for
from flask import json
from flask import request 
from main import extract
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/extract-utube-info', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return extract(request.data)

    else:
        return "415 Unsupported Media Type ;)"

if __name__ == '__main__':
    app.run()