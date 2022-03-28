from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name = 'about'),
    path('addlesson/', addlesson, name = 'addlesson'),
    path('addstudent/', addstudent, name = 'addstudent'),
    path('addgroup/', addgroup, name = 'addgroup'),
    path('addmarks/<int:lessonid>/', addmarks, name = 'addmarks')
]