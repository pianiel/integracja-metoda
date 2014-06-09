import os
from flask import Flask, request
from analyzer import *

app = Flask(__name__)

def sendResult(result):
    #TODO implement
    pass

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/generator', methods=['POST'])
def generate():
    print 'INPUT: ', request.json
    result = Analyzer(request.json['series']).analyze()
    sendResult(result)
    print 'RESULT: ', result
    return '200'

if __name__ == '__main__':
    app.run(debug=True)
