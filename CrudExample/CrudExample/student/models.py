from django.db import models

# Create your models here.


class Student(models.Model):
    sid = models.CharField(max_length=20)
    sname = models.CharField(max_length=100)
    semail = models.EmailField()
    scontact = models.CharField(max_length=15)
    class Meta:
        dt_table = "student"