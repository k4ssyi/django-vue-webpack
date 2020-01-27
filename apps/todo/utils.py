from .models import Todo


class TodoQuerys:
    """ToDoモデルのクエリセット."""

    @classmethod
    def todo_list(cls):
        todos = Todo.objects.all()
        return todos
