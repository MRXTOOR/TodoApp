
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .models import Todo


# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list':todos, 'title':'Главная страница'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST.get['title']
    todo = Todo(title=title)
    todo.save()
    return redirect('index')
    