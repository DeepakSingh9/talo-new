from django import forms
from django.contrib.auth.models import User
from dashboard.models import Profile,Post,Skills,ProfileContact

class ImageUpload(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_image',)




class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','video',)


class AboutMeForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('about_me',)


class AddSkill(forms.ModelForm):
    class Meta:
        model=Skills
        fields=('name','level',)

class AddContact(forms.ModelForm):
    class Meta:
        model=ProfileContact
        fields=('phone','city',)
