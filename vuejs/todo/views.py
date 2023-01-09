import json
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render


def index(request):
    return render(request, 'todo/list.html')


def todo_fetch(request):
    todos = Todo.objects.all()
    todo_list = []
    for index, todo in enumerate(todos, start=1):
        todo_list.append({'id': index, 'title': todo.title, 'completed': todo.completed})

    return JsonResponse(todo_list, safe=False)


@csrf_exempt    # csrf 방식을 간단히 해제 시키는 전처리기
@require_POST   # POST 메서드를 사용했을 때만 뷰가 동작하도록 하기
def todo_save(request):
    if request.body:
        data = json.loads(request.body)
        if 'todos' in data:
            todos = data['todos']
            Todo.objects.all().delete()
            for todo in todos:
                print('todo', todo)
                form = TodoForm(todo)
                if form.is_valid():
                    form.save()

    return JsonResponse({})