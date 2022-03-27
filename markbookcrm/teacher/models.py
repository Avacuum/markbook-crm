from django.db import models

class Lessons(models.Model):
    title = models.CharField(max_length = 255)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True)
    link = models.TextField(blank = True)
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Students(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photos/")
    time_registration = models.DateField(auto_now_add = True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.name+" "+self.surname

    class Meta:
        verbose_name = "Ученики"
        verbose_name_plural = "Ученики"
        ordering = ['time_registration', 'name']

class Group(models.Model):
    groupName = models.CharField(max_length=50)
    group_time_registration = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.groupName

class Marks(models.Model):
    mark = models.SmallIntegerField()
    student = models.ForeignKey('Students', on_delete=models.PROTECT)
    lesson = models.ForeignKey('Lessons', on_delete=models.PROTECT)

    def __str__(self):
        return self.mark