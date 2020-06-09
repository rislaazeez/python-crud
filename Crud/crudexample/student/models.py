from django.db import models

# Create your models here.

class Student(models.Model):
    Rollno = models.CharField(max_length=20)
    Stud_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    stud_class = models.CharField(max_length=10)

    def __str__(self):
        return self.Stud_Name


#superuser password :1234