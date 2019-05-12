# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,Post,ProfileContact,Skills


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','description','profile_image']


class PostAdmin(admin.ModelAdmin):
    list_display=['video','title','profile']

class ContactAdmin(admin.ModelAdmin):
    list_display=['phone']

class SkillAdmin(admin.ModelAdmin):
    list_display=['name','level']



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ProfileContact,ContactAdmin)
admin.site.register(Skills,SkillAdmin)
# Register your models here.
