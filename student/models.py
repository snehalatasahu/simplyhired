from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    user=models.OneToOneField('auth.user',default="", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=128)
    email = models.EmailField()
    isStudent = models.BooleanField(default=True)

    def __str__(self):
        return self.name

