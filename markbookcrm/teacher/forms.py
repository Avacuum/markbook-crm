from django import forms   
from .models import *

class AddLessonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = "Выбрать группу"


    class Meta:
        model = Lessons
        fields = ['title','link','group']
        titleLable = "Тема урока"
        linkLable = "Ссылка на справочный материал"
        widgets = {
            'title': forms.TextInput(attrs={"placeholder":titleLable, "class" : "w-100"}),
            'link': forms.TextInput(attrs={"placeholder":linkLable, "class" : "w-100"}),
            'group': forms.Select(attrs={ "class" : "form-select"})

        }

class AddStudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].empty_label = "Выбрать группу"


    class Meta:
        model = Students
        fields = ['name','surname','group']
        nameLable = "Name"
        surnameLable = "Surname"
        widgets = {
            'name': forms.TextInput(attrs={"placeholder":nameLable, "class" : "w-100"}),
            'surname': forms.TextInput(attrs={"placeholder":surnameLable, "class" : "w-100"}),
            'group': forms.Select(attrs={ "class" : "form-select"})
        }

class AddGroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Group
        fields = ['groupName']
        groupNameLable = "Name"
        widgets = {
            'name': forms.TextInput(attrs={"placeholder":groupNameLable, "class" : "w-100"}),
            }