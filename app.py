
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/countup')
def countup():
    retr = ''
    for i in range(11):
        numb = str(i)
        retr = retr + f'Count: {numb}<br />'
    return retr

if __name__ == '__main__':
    app.run(debug=True)

