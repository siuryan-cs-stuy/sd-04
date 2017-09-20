from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Random number generator</h1><br><a href="/number">Get a random number</a>'

@app.route('/number')
def number():
    return 'Your random number is: ' + str(randint(0,10)) + '<br><br><a href="/number">Get another number</a><br><a href="/list">Get a list of numbers</a>'

@app.route('/list')
def list():
    retStr = ''
    for i in range(10):
        retStr += str(randint(0,10)) + '<br>'
    return retStr

if __name__ == '__main__':
    app.debug = True
    app.run()
