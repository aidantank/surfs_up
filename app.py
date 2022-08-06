# Import dependencies
from flask import Flask

# Create new Flask App Instance
app = Flask(__name__)

@app.route('/')
def welcome():
    print('Hello world')
    return 'Avaliable port: /test'

@app.route('/test')
def test():
    return 'This is not a drill!'