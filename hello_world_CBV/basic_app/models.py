from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal= models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)
    # related_name - foreign key is how a student points at which school they're related to
    # related_name is how an instance of School object can query over students that have pointers
    # directing at that instance of School class

    def __str__(self):
        return self.name