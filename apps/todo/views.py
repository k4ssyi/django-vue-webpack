from django.shortcuts import HttpResponse, render
from django.views.generic import View

from .utils import TodoQuerys


class TodoIndexView(View):
    def get(self, request, *args, **kwargs):
        todo_list = TodoQuerys.todo_list()
        print(todo_list)
        return render(request, 'todoList.html',
                      context={'todo_list': todo_list},)

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')
