import os, json, requests
from flask import Flask, request
from analyzer import *
from config import *

app = Flask(__name__)

def sendResult(data, result):
    output = {'input':data, 'output':result}
    toSend = json.dumps(output)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    print 'SENDING: ', toSend
    for url in OUTPUT_URLS:
        r = requests.post(url, data=toSend, headers=headers)
        print 'R: ', r

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/generator', methods=['POST'])
def generate():
    print 'INPUT: ', request.json
    result = Analyzer(request.json['series']).analyze()
    print 'RESULT: ', result
    sendResult(request.json, result)
    return '200'

if __name__ == '__main__':
    app.run(debug=True)
