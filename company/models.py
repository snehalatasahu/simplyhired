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

    class Meta:
        managed = True
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

class Profile(models.Model):
    objects = models.Manager()
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    pic = models.ImageField(upload_to="company/", blank=True, null=True)
    mob = models.CharField(blank=True, null=True, max_length=10)
    address = models.CharField(blank=True, null=True, max_length=128)
    website = models.URLField(blank=True, null=True, max_length = 200)

    no_of_employees = models.IntegerField(default=0, null=True)
    internship_post = models.IntegerField(default=0, null=True)
    interns_hired = models.IntegerField(default=0, null=True)

    facebook_link = models.URLField(blank=True, null=True, max_length = 200)
    twitter_link = models.URLField(blank=True, null=True, max_length = 200)
    linkedin_link = models.URLField(blank=True, null=True, max_length = 200)
    youtube_link = models.URLField(blank=True, null=True, max_length = 200)

    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company.name

    class Meta:
        managed = True
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

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

