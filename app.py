from flask import Flask, request
import haml
import mako.template
import mako.lookup
from waitress import serve
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

lookup = mako.lookup.TemplateLookup(["views"], preprocessor=haml.preprocessor)

TEMPLATES = {}

def lookup_template(template_name):
    template = TEMPLATES.get(template_name)
    if template: return template
    template = lookup.get_template(f'{template_name}.haml')
    TEMPLATES[template_name] = template
    return template


def render(template_name, **args):
    template = lookup_template(template_name)
    return template.render(**args)

@app.route('/')
def hello():
    r.set('foo', 'bar')
    # foo = request.args.get('foo')
    test = "1234"
    foo = r.get('foo')
    # template = lookup.get_template('home.haml')
    # return template.render(test=test, foo=foo)
    return render("home", test=test, foo=foo)

# @app.route('/foo', methods=["POST"])
# def foo():

if __name__ == '__main__':
    app.run()
    # serve(app, host='0.0.0.0', port=3000)
