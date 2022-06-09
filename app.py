from flask import Flask
from random import randint

app = Flask(__name__)

def random_number_generator():
    range_start = 10**(6-1)
    range_end = (10**6)-1
    return randint(range_start, range_end)

@app.route('/')
def hello_world():
    random_number=str(random_number_generator())
    return '<h1>Hello World %s </h1>' %random_number


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)