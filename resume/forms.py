from django import forms
from .models import Educations,Project,WorkExperience
import datetime

class BioForm(forms.ModelForm):
    class Meta:
        model=Educations
        fields=('masters_education_from','masters_education_till',
                'masters_college_name',)

class WorkExperienceForm(forms.ModelForm):

    class Meta:
        model=WorkExperience
        fields=('organisation','designation',
                'worked_from','worked_till',
                'current','describe',)


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('title','year',
                'link','organisation',
                'position','description',)

'''


class InterestsForm(forms.ModelForm):

    class Meta:
        model=Interest
        fields=('name',)

class CertificationsForm(forms.ModelForm):

    class Meta:
        model=Certification
        fields=('title','year',
                'description','link',
                'cert_image',)




'''