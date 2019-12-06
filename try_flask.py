from flask import Flask
import haml
import mako.template
import mako.lookup

app = Flask(__name__)

lookup = mako.lookup.TemplateLookup(["views"],
    preprocessor=haml.preprocessor
)

@app.route('/')
def hello():
    foo = request.args.get('foo') /?foo=bar
    test = "1234"
    template = lookup.get_template('home.haml')
    return template.render(test=test, foo=foo)

@app.route('/foo', methods=["POST"])
def foo():


if __name__ == '__main__':
    app.run()
