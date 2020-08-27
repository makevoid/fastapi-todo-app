from flask import Flask, request
import haml
import mako.template
import mako.lookup
from waitress import serve

app = Flask(__name__)

lookup = mako.lookup.TemplateLookup(["views"],
    preprocessor=haml.preprocessor
)

@app.route('/')
def hello():
    foo = request.args.get('foo')
    test = "1234"
    template = lookup.get_template('home.haml')
    return template.render(test=test, foo=foo)

# @app.route('/foo', methods=["POST"])
# def foo():

if __name__ == '__main__':
    app.run()
    # serve(app, host='0.0.0.0', port=3000)
