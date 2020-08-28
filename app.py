import json
from flask import Flask, request
from waitress import serve
from env import R, flask_options
from lib import render

app = Flask(__name__, **flask_options)

@app.route('/')
def root():
    R.set('foo', 'bar')
    # foo = request.args.get('foo')
    test = "1234"
    foo = R.get('foo')
    return render("home", test=test, foo=foo)

@app.route('/hello')
def hello2():
    return render("page2")

class Todo(object):
    """Todo items model"""

    def __init__(self, text, checked=false):
        super(Todo, self).__init__()
        self.text = text
        self.checked = checked
        todos_count = R.incr('todos_count')
        self.id = todos_count
        save()

    def check():
        self.checked = !self.checked
        save()
        return self

    def update_text(text):
        self.text = text
        save()
        return self

    def save():
        todo = json.dumps(self.__dict__)
        R.set(f'todos:${id}', todo)
        return self

    @classmethod
    def get(todo_id)
        todo = R.get(f'todos:${todo_id}')
        todo = json.loads(todo)
        todo = new Todo
        return todo

    @classmethod
    def all()
        todos_count = R.get('todos_count')
        todos_count = int(todos_count)
        todos = []
        for i in range(todos_count):
            todo = self.get(i)
            todos.push(todo)
        return todos

@app.route('/todos', methods=["POST"])
def todo_create():
    todo = Todo(text)
    print(f'Todo created: {todo.__dict__}')
    redirect(url_for('root'))

@app.route('/todos/<int:todo_id>', methods=["POST"])
def todo_update(todo_id):
    todo = Todo(text)
    print(f'Todo created: {todo.__dict__}')
    redirect(url_for('root'))


if __name__ == '__main__':
    app.run()
    # serve(app, host='0.0.0.0', port=3000)
