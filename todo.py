from json import loads, dumps

from env import R

class Todo(object):
    """Todo items model"""

    def __init__(self, id, text, checked=False):
        self.id = id
        self.text = text
        self.checked = checked

    # check / uncheck
    def check(self):
        self.checked = not self.checked
        self.save()
        return self

    def update_text(self, text):
        self.text = text
        self.save()
        return self

    def save(self):
        todo = dumps(self.__dict__)
        R.set(f'todos:{self.id}', todo)
        return self

    @staticmethod
    def create(text, checked=False):
        todos_count = R.incr('todos_count')
        id = todos_count
        todo = Todo(id, text)
        todo.save()
        return todo

    @classmethod
    def get(cls, todo_id):
        todo = R.get(f'todos:{todo_id}')
        todo = loads(todo)
        todo = cls(**todo)
        return todo

    @staticmethod
    def all():
        todos_count = R.get('todos_count') or 0
        todos_count = int(todos_count)
        todos = []
        for i in range(1, todos_count+1):
            todo = Todo.get(i)
            todos.append(todo)
        return todos
