from django import forms
from .models import Bio,Project,Certification,Interest,WorkExperience

class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        fields=('highest_degree','education_from')


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=('title','year',
                'link','organisation',
                'position','description',)

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

class WorkExperienceForm(forms.ModelForm):

    class Meta:
        model=WorkExperience
        fields=('organisation','designation',
                'worked_from','worked_till',
                'current','describe',)


