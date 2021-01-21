import os
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index() :
    return render_template('index.html')



if __name__=='__main__' :
    app.run(debug=True)
