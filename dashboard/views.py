# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import ImageUpload,PostForm,AboutMeForm,AddSkill,AddContact
from dashboard.models import Profile,Skills,ProfileContact
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def home(request):
    return render(request,'dashboard/home.html',{})



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
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = user
            post.save()
            return redirect('/')
        else:
            print (form.errors)
    else:
        form = PostForm()
    return render(request, 'dashboard/uploadskills.html', {'form': form})


def aboutme(request,pk):
    profile=Profile.objects.get(pk=pk)
    if request.method=='POST':
        form=AboutMeForm(request.POST)
        if form.is_valid():
            aboutme=form.save(commit=False)
            profile.about_me=request.POST['about_me']
            profile.user=request.user
            profile.save()
            return redirect('/')
        else:
            print (form.errors)
    else:
        form=AboutMeForm()
    return render(request,'dashboard/aboutme.html',{'form':form})



def edit_aboutme(request,pk):
    profile=get_object_or_404(Profile,pk=pk)
    if request.method=='POST':
        form = AboutMeForm(request.POST, instance=profile)
        if form.is_valid():
            aboutme=form.save(commit=False)
            profile.about_me=request.POST['about_me']
            profile.user=request.user
            profile.save()
            return redirect('/')
        else:
            form.errors
    else:
        form=AboutMeForm(instance=profile)
    return render(request,'dashboard/aboutme.html',{'form':form})




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
            skill.save()
            return redirect('/')
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
    skill= get_object_or_404(Skills,pk=pk)
    skill.delete()
    return redirect('/')



def addcontact(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method =='POST':
        form=AddContact(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.profile=profile
            contact.save()
            return redirect('/')
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddContact()
    return render(request,'dashboard/addcontact.html',{'form':form})


def edit_contact(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    Contact=ProfileContact.objects.get(pk=pk)
    if request.method == 'POST':
        form=AddContact(request.POST,instance=Contact)
        if form.is_valid():
            form.save(commit=False)
            form.profile=profile
            form.save()
            return redirect('/')
        else:
            HttpResponse('form is incomplete')
    else:
        form=AddContact(instance=Contact)
    return render(request,'dashboard/addcontact.html',{'form':form})



def delete_contact(request,pk):
    contact= get_object_or_404(ProfileContact,pk=pk)
    contact.delete()
    return redirect('/')

