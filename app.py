import os
from flask import Flask, request, redirect, url_for, render_template, json, send_from_directory
import random

app = Flask(__name__)

data = []
question = ""
answer = ""

@app.route('/', methods = ['POST', 'GET'])
def index():
    data = []
    q = ""
    a = ""

    ## Addition Data
    for i in range(0,6):
        for j in range(0,5):
            if i+j < 10 and i+j > -1:
                q = str(i) + " + " + str(j)
                s = i+j
                a = str(s)
                value = [q, a]
                data.append(value)

    ## Subtraction Data 
    for i in range(0,10):
        for j in range(0,10):
            if i-j < 10 and i-j > -1:
                q = str(i) + " - " + str(j)
                s = i-j
                a = str(s)
                value = [q, a]
                data.append(value)

    randomNumber = random.randint(0, len(data))
    question = data[randomNumber][0]
    answer = data[randomNumber][1]
    data.pop(randomNumber)
    
    return render_template('index.html', question = question, answer = answer)


@app.route('/models/model.json', methods = ['POST', 'GET'])
def test():
    f = open("./model.json")
    data = json.load(f) 
    f.close()
    return json.dumps(data)


if __name__=='__main__' :
    app.run(debug=True)
