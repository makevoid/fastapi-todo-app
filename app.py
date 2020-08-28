from flask import Flask, request, redirect, url_for, jsonify
from waitress import serve
from env import R, flask_options
from lib import render
from todo import Todo

app = Flask(__name__, **flask_options)

@app.route('/')
def root():
    todos = Todo.all()
    return render("home", todos=todos)

@app.route('/hello')
def hello2():
    return render("page2")

@app.route('/todos', methods=["POST"])
def todo_create():
    # text = request.form.get('item')
    text = request.form['item']
    todo = Todo.create(text)
    print(f'Todo created: {todo.__dict__}')
    return redirect(url_for('root'))

@app.route('/todos/<int:todo_id>', methods=["POST"])
def todo_update(todo_id):
    text = request.form['item']
    todo = Todo.get(todoId)
    todo.update_text(text)
    print(f'Todo created: {todo.__dict__}')
    return redirect(url_for('root'))

@app.route('/todos/<int:todo_id>/check', methods=["POST"])
def todo_check(todo_id):
    todo = Todo.get(todo_id)
    todo.check()
    print(f'Todo {todo.id} checked/unchecked')
    data = jsonify(todo.__dict__)
    return data


if __name__ == '__main__':
    app.run(port=3000)
    # serve(app, host='0.0.0.0', port=3000)
