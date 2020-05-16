from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal= models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    # this method tells which page to render once user submits a filled-in form
    # no validaion of provided data, though - this has to be manually coded
    def get_absolute_url(self):
        return reverse("basic_app:detail", kwargs={"pk": self.pk})
    


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)
    # related_name - foreign key is how a student points at which school they're related to
    # related_name is how an instance of School object can query over students that have pointers
    # directing at that instance of School class

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:student_detail", kwargs={"pk": self.pk})
    