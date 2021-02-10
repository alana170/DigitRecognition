import os
from flask import Flask, request, redirect, url_for, render_template, json

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index() :
    return render_template('index.html')


@app.route('/models/model.json', methods = ['POST', 'GET'])
def test() :
    f = open('models/model.json')
    data = json.load(f) 
    f.close()
    return json.dumps(data)


if __name__=='__main__' :
    app.run(debug=True)
