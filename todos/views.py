# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

#homepage
def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

#details page
def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

#add todos page
def add(request):
    if(request.method == 'POST'):

        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')

    else:
        return render(request, 'add.html')
