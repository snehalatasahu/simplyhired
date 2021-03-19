from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.
class Student(models.Model):
    objects = models.Manager()
    user=models.OneToOneField('auth.user',default="", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=128)
    email = models.EmailField()
    isStudent = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    objects = models.Manager()
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    address = models.CharField(default='India', max_length=128)
    mob = models.CharField(max_length=10)
    skills = models.TextField()
    pic = models.ImageField()


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
