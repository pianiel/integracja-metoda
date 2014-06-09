import os, json, requests
from flask import Flask, request
from analyzer import *

app = Flask(__name__)

def sendResult(data, result):
    output = {'input':data, 'output':result}
    toSend = json.dumps(output)
    print 'SENDING: ', toSend
    url = 'integracja.herokuapp.com/rest/sequences'
    r = requests.post(url, data=toSend)

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
