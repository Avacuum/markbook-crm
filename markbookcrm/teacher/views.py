from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from .forms import *


def index(request):
    groups = Group.objects.all()
    return render(request, 'teacher/index.html', {'title':'Главная',  "groups":groups})

def about(request):
    return render(request, 'teacher/about.html', {'title':'О сайте'})

def addlesson(request):
    form = AddLessonForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            group = form.cleaned_data['group']
            students = Students.objects.filter(group_id = group.id)
            return render(request, 'teacher/addmarks.html', {'group':group, 'students': students})
    else:
        return render(request, 'teacher/addlesson.html', {'title':'Добавить урок', 'form':form})

def addstudent(request):
    form = AddStudentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            group = form.cleaned_data['group']
            students = Students.objects.filter(group_id = group.id)
            return redirect('home')
    else:
        return render(request, 'teacher/addstudent.html', {'title':'Добавить Ученика', 'form':form})

def addgroup(request):
    form = AddGroupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            #print(form.cleaned_data)
            #group = form.cleaned_data['group']
            #students = Students.objects.filter(group_id = group.id)
            return redirect('home')
    else:
        return render(request, 'teacher/addgroup.html', {'title':'Create new group', 'form':form})

def pageNotFound(request, exception):
    return HttpResponseNotFound("pososee")