# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import BioForm,WorkExperienceForm,ProjectForm
#,InterestsForm,CertificationsForm
from dashboard.models import Profile
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404,redirect
from .models import WorkExperience,Project

# Create your views here.

def resume(request,username):
    user=request.user
    profile=Profile.objects.get(user=user)
    masters=profile.masters_degree_name
    bachelors=profile.bachelors_degree
    high_school=profile.High_School_degree
    junior_school=profile.Junior_degree
    return render(request,'resume/resume.html',{'user':user,'profile':profile,'masters':masters,'bachelors':bachelors,'high_school':high_school,'junior_school':junior_school})


def workexp(request):
    user=request.user
    profile=get_object_or_404(Profile,user=user)
    if request.method== 'POST':
        form=WorkExperienceForm(request.POST)
        if form.is_valid():
            workex=form.save(commit=False)
            workex.profile=profile
            workex.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=WorkExperienceForm()
    return render(request,'resume/workexp.html',{'form':form,'profile':profile})


def edit_workexp(request,pk):
    user = request.user
    workex = WorkExperience.objects.get(pk=pk)
    profile=Profile.objects.get(user=user)
    if request.method == 'POST':
        form=WorkExperienceForm(request.POST,instance=workex)
        if form.is_valid():
            workex=form.save(commit=False)
            workex.profile=profile
            workex.save()
            return redirect('resume',username=user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=WorkExperienceForm(instance=workex)

    return render(request,'resume/workexp.html',{'form':form})

def delete_workexp(request,pk):

    workexperience=get_object_or_404(WorkExperience,pk=pk)
    workexperience.delete()
    return redirect('resume',username=workexperience.profile.user.username)



def project(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile=profile
            project.save()
            return redirect('resume',username=profile.user.username)
        else:
            HttpResponse('please fill the form')
    else:
        form=ProjectForm()
    return render(request,'resume/projects.html',{'form':form})


def edit_project(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    project=Project.objects.get(pk=pk)
    if request.method == 'POST':
        form=ProjectForm(request.POST,instance=project)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile=profile
            project.save()
            return redirect('resume')
        else:
            HttpResponse('please fill the form')
    else:
        form=ProjectForm(instance=project)
    return render(request,'resume/projects.html',{'form':form})

def delete_project(request,pk):
    project=get_object_or_404(Project,pk=pk)
    project.delete()
    return redirect('resume')





'''
def bio(request):
    if request.method=='POST':
        form=BioForm(request.POST)
        user=request.user
        if form.is_valid():
            bio=form.save(commit=False)
            bio.user=user
            bio.save()
            return redirect('resume',username=user.username)
        else:
            HttpResponse('please fill the form properly')
    else:
        form=BioForm()
    return render(request,'resume/bio.html',{'form':form})'''



'''
def edit_bio(request,pk):
    bio=get_object_or_404(Educations,pk=pk)
    if request.method=='POST':
        form=BioForm(request.POST,instance=bio)
        user=request.user
        if form.is_valid():
            bio=form.save(commit=False)
            bio.save()
            return redirect('resume',username=bio.user.username)
        else:
            HttpResponse('fill the form correctly')
    else:
        form=BioForm(instance=bio)
    return render(request,'resume/bio.html',{'form':form})'''

'''
def certification(request):
    if request.method == 'POST':
        form=CertificationsForm(request.POST,request.FILES)
        user=request.user
        bio=Bio.objects.get(user=user)
        if form.is_valid():
            certification=form.save(commit=False)
            certification.bio=bio
            certification.save()
            return redirect('resume')
        else:
            HttpResponse('form is incomplete ')
    else:
        form=CertificationsForm()
    return render(request,'resume/certification.html',{'form':form})



def edit_certification(request,pk):
    cert=get_object_or_404(Certification,pk=pk)
    user = request.user
    bio = Bio.objects.get(user=user)
    if request.method == 'POST':
        form=CertificationsForm(request.POST,request.FILES,instance=cert)

        if form.is_valid():
            cert=form.save(commit=False)
            cert.cert_image = request.FILES('file')
            cert.bio=bio
            cert.save()
            return redirect('resume')
        else:
            HttpResponse('form is incomplete ')
    else:
        form=CertificationsForm(instance=cert)
    return render(request,'resume/certification.html',{'form':form})



def interest(request):
    user=request.user
    bio=Bio.objects.get(user=user)
    if request.method =='POST':
        form=InterestsForm(request.POST)
        if form.is_valid():
            interest=form.save(commit=False)
            interest.bio=bio
            interest.save()
            return render('resume')
        else:
            HttpResponse('form is incomplete')
    else:
        form=InterestsForm()
    return render(request,'resume/interest.html',{'form':form})


def edit_interest(request,pk):
    user=request.user
    bio=Bio.objects.get(user=user)
    interest=Interest.objects.get(pk=pk)
    if request.method == 'POST':
        form=InterestsForm(request.POST,instance=interest)
        if form.is_valid():
            form.save(commit=False)
            form.bio=bio
            form.save()
            return render('resume')
        else:
            HttpResponse('form is incomplete')
    else:
        form=InterestsForm(instance=interest)
    return render(request,'resume/interest.html',{'form':form})




def delete_certification(request,pk):
    certification=get_object_or_404(Certification,pk=pk)
    certification.delete()
    return redirect('resume')






def delete_interest(request,pk):
    interest= get_object_or_404(Interest,pk=pk)
    interest.delete()
    return redirect('resume')


def delete_bio(request,pk):
    bio = get_object_or_404(Bio,pk=pk)
    user = bio.user
    bio.delete()
    return redirect('resume',username=user.username)'''