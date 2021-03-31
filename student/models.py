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
    address = models.CharField(blank=True, null=True, max_length=128)
    mob = models.CharField(blank=True, null=True, max_length=10)
    skills = models.TextField(blank=True, null=True)
    pic = models.ImageField(upload_to="student/", blank=True, null=True)
    college = models.CharField(blank=True, null=True, max_length=128)
    grad_year = models.CharField(blank=True, null=True, max_length=10)
    cgpa = models.CharField(blank=True, null=True, max_length=5)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
