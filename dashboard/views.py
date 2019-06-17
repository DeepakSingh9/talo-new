# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import ImageUpload,PostForm,AboutMeForm,AddSkill,AddContact,AddEducation
from dashboard.models import Profile,Skills,ProfileContact
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request,username):
    user=request.user
    profile=Profile.objects.get(user=user)
    if username != user.username:
        return render(request,'dashboard/profile.html',{'profile':profile,'user':user})
    else:
        return render(request,'dashboard/home.html',{'user':user,'profile':profile})


@login_required()
def profile_image_upload(request,pk):
    image=False
    user = request.user
    profile = get_object_or_404(Profile, pk=user.id)
    if request.method =='POST':
        form = ImageUpload(request.POST,request.FILES)
        if form.is_valid():
            profile.profile_image=request.FILES['file']
            profile.save()
            return redirect('/')
        else:
            return HttpResponse('please choose an image')
    else:
        form=ImageUpload()
    return render(request,'dashboard/image_upload.html',{'form':form,'profile':profile,'user':user,'image':image})





def uploadskills(request):
    if request.method == 'POST':
        user = request.user
        profile=Profile.objects.get(user=user)
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('home',username=user.username)
        else:
            print (form.errors)
    else:
        form = PostForm()
    return render(request, 'dashboard/uploadvideo.html', {'form': form,})


def aboutme(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=Profile.objects.get(user=user)

    if request.method=='POST':
        form=AboutMeForm(request.POST)
        if form.is_valid():
            aboutme=form.save(commit=False)
            profile.about_me=request.POST['about_me']
            profile.user=request.user
            profile.save()
            return redirect('home',username=user.username)
        else:
            print (form.errors)
    else:
        form=AboutMeForm()
    return render(request,'dashboard/aboutme.html',{'form':form})



def edit_aboutme(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=get_object_or_404(Profile,user=user)

    if request.method=='POST':
        form = AboutMeForm(request.POST, instance=profile)
        if form.is_valid():
            aboutme=form.save(commit=False)
            profile.about_me=request.POST['about_me']
            profile.user=request.user
            profile.save()
            return redirect('home',username=user.username)
        else:
            form.errors
    else:
        form=AboutMeForm(instance=profile)
    return render(request,'dashboard/aboutme.html',{'form':form,'profile':profile})




def learning(request):
    return render(request,'dashboard/learning.html',{})


def addskills(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method =='POST':
        form=AddSkill(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.profile=profile
            skill.name=request.POST['name']
            skill.save()
            return redirect('home',username=user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddSkill()
    return render(request,'dashboard/uploadskills.html',{'form':form})


def edit_skill(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    skill=Skills.objects.get(pk=pk)
    if request.method == 'POST':
        form=AddSkill(request.POST,instance=skill)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('/')
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddSkill(instance=skill)
    return render(request,'dashboard/uploadskills.html',{'form':form})

def delete_skill(request,pk):
    user=request.user
    skill= get_object_or_404(Skills,pk=pk)
    skill.delete()
    return redirect('home',username=user.username)



def addcontact(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method =='POST':
        form=AddContact(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.profile=profile
            contact.save()
            return redirect('home',username=user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddContact()
    return render(request,'dashboard/addcontact.html',{'form':form})


def edit_contact(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    Contact=ProfileContact.objects.get(profile=profile)
    if request.method == 'POST':
        form=AddContact(request.POST,instance=Contact)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('home',username=user.username)
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddContact(instance=Contact)
    return render(request,'dashboard/addcontact.html',{'form':form})



def delete_contact(request,pk):
    contact= get_object_or_404(ProfileContact,pk=pk)
    contact.delete()
    return redirect('/')

@login_required()
def follow(request,pk):
    profile=get_object_or_404(User,id=pk)
    user=request.user
    if user.is_authenticated():
        if user.id != get_object_or_404(User,id=pk):
            try:
                profile.profile.followed_by.add(user.profile)
                following = True
                return redirect('home',username=profile.username)
            except ObjectDoesNotExist:
                return HttpResponse('The author you are following has removed the account')

    return redirect(request,'/',{})


def addeducation(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=Profile.objects.get(user=user)

    if request.method=='POST':
        form=AddEducation(request.POST)
        if form.is_valid():
            addeducation=form.save(commit=False)
            profile.masters_degree_name=request.POST['masters_degree_name']
            profile.masters_college_name=request.POST['masters_college_name']
            profile.masters_education_from=request.POST['masters_education_from']
            profile.masters_education_till=request.POST['masters_education_till']
            profile.bachelors_degree=request.POST['bachelors_degree']
            profile.bachelors_college_name=request.POST['bachelors_college_name']
            profile.bachelors_education_from=request.POST['bachelors_education_from']
            profile.bachelors_education_till=request.POST['bachelors_education_till']
            profile.High_School_degree=request.POST['High_School_degree']
            profile.High_School_name=request.POST['High_School_name']
            profile.High_School_from=request.POST['High_School_from']
            profile.High_School_till=request.POST['High_School_till']
            profile.Junior_degree=request.POST['Junior_degree']
            profile.Junior_School_name=request.POST['Junior_School_name']
            profile.Junior_School_from=request.POST['Junior_School_from']
            profile.Junior_School_till=request.POST['Junior_School_till']
            profile.user=request.user
            profile.save()
            return redirect('resume',username=user.username)
        else:
            print (form.errors)
    else:
        form=AddEducation()
    return render(request,'dashboard/addeducation.html',{'form':form})


def edit_education(request,pk):
    user = get_object_or_404(User, pk=pk)
    profile=get_object_or_404(Profile,user=user)

    if request.method=='POST':
        form = AddEducation(request.POST, instance=profile)
        if form.is_valid():
            addeducation=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect('resume',username=user.username)
        else:
           form.errors
    else:
        form=AddEducation(instance=profile)
    return render(request,'dashboard/addeducation.html',{'form':form,'profile':profile})