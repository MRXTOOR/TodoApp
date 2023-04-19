
from django.shortcuts import render

from .models import Todo


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list':todos, 'title':'Главная страница'})