from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    objects = models.Manager()
    user=models.OneToOneField('auth.user',default="", on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=128)
    email = models.EmailField()
    isCompany = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Internship(models.Model):
    objects = models.Manager()
    company = models.ForeignKey( 'Company' , on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    place = models.CharField(max_length=128)
    duration = models.CharField(max_length=128)
    stipend = models.CharField(max_length=128)
    # apply_by = models.DateField() 
    no_of_openings =  models.IntegerField()
    perks = models.CharField(max_length=128)
    skills = models.CharField(max_length=128)
    about_internship = models.TextField()
    who_can_apply = models.TextField()
    
   

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Internship'
        verbose_name_plural = 'Internships'

