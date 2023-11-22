from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.

def addTask (request):
    # print(request.POST)
    task = request.POST.get('task')
    Task.objects.create(task = task)
    print(task)
    #return HttpResponse('hai')
    return redirect ('home')

    # Task.objects.create(task = task)

def mark_as_done (request,pk):
    # genral method then after we need write the if condition in general method to check weather a flie is present or not
    # task_completed = Task.objects.get(pk=pk)
    # task_completed.is_completed =  True
    # task_completed.save()
# same work can be done in single line  code
    task_completed = get_object_or_404(Task, pk=pk)
    task_completed.is_completed =  True
    task_completed.save()

    
    return redirect ('home')

def mark_as_undone (request,pk):
    print(pk)
    task_not_completed = get_object_or_404(Task, pk=pk)
    task_not_completed.is_completed =  False
    task_not_completed.save()
    # return HttpResponse(pk)
    return redirect ('home')

def delete (request,pk):
    delete_task =  get_object_or_404(Task, pk=pk)
    delete_task.delete()
    # return HttpResponse(pk)
    return redirect ('home')

def edit_task (request,pk):
    get_task =  get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        edited_task = request.POST.get ('task')
        get_task.task = edited_task
        get_task.save()
        print(edited_task)
        return redirect ('home')    
    else:
        context = {
            'get_task': get_task
        }
        return render (request,'edit_task.html',context)

