from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import *
from .forms import *
from django.forms import formset_factory



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
            lessonid = Lessons.objects.latest('id').id
            return redirect(f'/addmarks/{lessonid}')
    else:
        return render(request, 'teacher/addlesson.html', {'title':'Добавить урок', 'form':form})

def addmarks(request, lessonid):
    lesson = Lessons.objects.get(id = lessonid)
    group = Group.objects.get(id = lesson.group_id)
    students = Students.objects.filter(group = group.id)
    print(lesson, group, len(students))
    
    marksFormSet = formset_factory(AddMarkForm, extra=len(students))
    context = {}
    context['formset'] = marksFormSet()
    form = AddMarkForm(request.POST)
    if form.is_valid():
        print(True)
    else:
        print(False)

    #return render(request, 'teacher/addmarks.html', context, {'lessonid':lessonid, 'lesson': lesson, 'group': group, 'students':students})
    return render(request, 'teacher/addmarks.html', {'lessonid':lessonid, 'lesson': lesson, 'group': group, 'students':students, 'formset':marksFormSet})


def addstudent(request):
    form = AddStudentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
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