from django.shortcuts import render,redirect
from .forms import todo
from .models import Todo
from django.views.decorators.http import require_POST
def index(request):
    mytodo = Todo.objects.order_by('id')
    form = todo()  
    context = {'mytodo': mytodo, 'form':form}
    return render(request,'Todo/Todo.html',context)

@require_POST #Function Decorator inhance the functionality of this function As todo.html handle two request
def newtodo(request):
    form = todo(request.POST)
    if form.is_valid():
        my_new_todo = Todo(text=request.POST['text'])
        my_new_todo.save()
    return redirect('Home')
    

def addtodo(request,todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()
    return redirect('Home')
def deleteall(request):
    Todo.objects.all().delete()
    return redirect('Home')
def deletetodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('Home')

