from django.db import models
from django.contrib.auth.models import User
import datetime
from dashboard.models import Profile

# Create your models here.
'''
class Bio(models.Model):
    Degree_choice=(('High School','HIGH SCHOOL'),('undergrad','UNDERGRAD'),('postgrad','POSTGRAD'),)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    masters_degree_name=models.CharField(max_length=150,blank=True,default='')
    masters_college_name=models.CharField(max_length=150,blank=True)
    masters_education_from = models.DateField(default=datetime.date.today)
    masters_education_till=models.DateField(default=datetime.date.today)
    bachelors_degree = models.CharField(max_length=150,blank=True)
    bachelors_college_name = models.CharField(max_length=150, blank=True)
    bachelors_education_from = models.DateField(default=datetime.date.today)
    bachelors_education_till = models.DateField(default=datetime.date.today)
    High_School_degree = models.CharField(max_length=150,blank=True)
    High_School_name = models.CharField(max_length=150, blank=True)
    High_School_from = models.DateField(default=datetime.date.today)
    High_School_till = models.DateField(default=datetime.date.today)
    Junior_degree = models.CharField(max_length=150,blank=True)
    Junior_School_name = models.CharField(max_length=150, blank=True)
    Junior_School_from = models.DateField(default=datetime.date.today)
    Junior_School_till = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username'''


class Educations(models.Model):
    Degree_choice=(('High School','HIGH SCHOOL'),('undergrad','UNDERGRAD'),('postgrad','POSTGRAD'),)
    user=models.OneToOneField(Profile,on_delete=models.CASCADE)
    masters_degree_name=models.CharField(max_length=150,blank=True,default='')
    masters_college_name=models.CharField(max_length=150,blank=True)
    masters_education_from = models.DateField(default=datetime.date.today)
    masters_education_till=models.DateField(default=datetime.date.today)
    bachelors_degree = models.CharField(max_length=150,blank=True)
    bachelors_college_name = models.CharField(max_length=150, blank=True)
    bachelors_education_from = models.DateField(default=datetime.date.today)
    bachelors_education_till = models.DateField(default=datetime.date.today)
    High_School_degree = models.CharField(max_length=150,blank=True)
    High_School_name = models.CharField(max_length=150, blank=True)
    High_School_from = models.DateField(default=datetime.date.today)
    High_School_till = models.DateField(default=datetime.date.today)
    Junior_degree = models.CharField(max_length=150,blank=True)
    Junior_School_name = models.CharField(max_length=150, blank=True)
    Junior_School_from = models.DateField(default=datetime.date.today)
    Junior_School_till = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
    title= models.CharField(max_length=128)
    year = models.DateField()
    description = models.TextField()
    link = models.URLField(blank=True)
    organisation=models.CharField(max_length=128,blank=True)
    position=models.CharField(max_length=128,blank=True)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
    organisation=models.CharField(max_length=128,blank=True,null=True)
    designation=models.CharField(max_length=128,blank=True,null=True)
    worked_from=models.DateField()
    worked_till=models.DateField()
    current=models.BooleanField(default=False)
    describe=models.TextField(blank=True)

    def __str__(self):
        return self.organisation


'''

class Certification(models.Model):
    education=models.ForeignKey(Education,on_delete=models.CASCADE,)
    title=models.CharField(max_length=128)
    year=models.DateField()
    description=models.TextField()
    link=models.URLField(blank=True)
    cert_image=models.FileField(upload_to='cert_images/',blank=True)

    def __str__(self):
        return self.title



class Interest(models.Model):
    education=models.ForeignKey(Education,on_delete=models.CASCADE,)
    name=models.CharField(max_length=128,blank=True)


    def __str__(self):
        return self.name




'''