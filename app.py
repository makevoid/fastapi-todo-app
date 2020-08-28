from flask import Flask, request
from waitress import serve
from env import R
from lib import render

app = Flask(__name__)

@app.route('/')
def hello():
    R.set('foo', 'bar')
    # foo = request.args.get('foo')
    test = "1234"
    foo = R.get('foo')
    return render("home", test=test, foo=foo)

# @app.route('/foo', methods=["POST"])
# def foo():

if __name__ == '__main__':
    app.run()
    # serve(app, host='0.0.0.0', port=3000)
