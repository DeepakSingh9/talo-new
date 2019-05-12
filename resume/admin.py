# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bio,Certification,Interest,WorkExperience,Project

# Register your models here.

class BioAdmin(admin.ModelAdmin):
    list_display = ['user','highest_degree']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['bio','title','year','description','link','organisation','position']

class WorkexpAdmin(admin.ModelAdmin):
    list_display = ['bio','organisation','designation','worked_from','worked_till','current','describe']



class CertificationAdmin(admin.ModelAdmin):
    list_display = ['bio','title','link','cert_image','description','year']


class InterestAdmin(admin.ModelAdmin):
    list_display = ['bio','name']


admin.site.register(Certification,CertificationAdmin)
admin.site.register(WorkExperience,WorkexpAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Bio, BioAdmin)
admin.site.register(Interest,InterestAdmin)

