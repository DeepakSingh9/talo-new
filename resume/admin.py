# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Educations,Project,WorkExperience,Certification,Interest

# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display = ['user','masters_college_name','masters_education_from','masters_education_till']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['profile','title','year','description','link','position']

class WorkexpAdmin(admin.ModelAdmin):
    list_display = ['profile','organisation','designation','worked_from','worked_till','current','describe']


class CertificationAdmin(admin.ModelAdmin):
    list_display = ['profile','title','link','cert_image','year']

class InterestAdmin(admin.ModelAdmin):
    list_display = ['profile','interest']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Educations, EducationAdmin)
admin.site.register(WorkExperience,WorkexpAdmin)
admin.site.register(Certification,CertificationAdmin)
admin.site.register(Interest,InterestAdmin)


