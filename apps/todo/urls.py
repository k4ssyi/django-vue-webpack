from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = (
    # ホーム画面(メール)
    path('', views.TodoIndexView.as_view(), name='todo_index'),
)
