
from django.shortcuts import render

from .models import Todo


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todolist':todos, 'title':'Главная страница'})