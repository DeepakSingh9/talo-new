 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from dashboard.models import Profile
from .forms import LoginForm, RegisterationForm


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home',username=user.username)
            else:
                return HttpResponse('Your account is disabled')
        else:
            return HttpResponse('Invalid login details')
    return render(request,'', {})




def user_registration(request):
    if request.method == 'POST':
        userlogin = LoginForm(request.POST)
        userregister = RegisterationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        if userlogin.is_valid() and userregister.is_valid():
            user = userlogin.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = userregister.save(commit=False)
            profile.user = user
            profile.save()

            login(request, authenticate(username=userlogin.cleaned_data['username'],
                                        password=userlogin.cleaned_data['password']))
            return redirect('/')
        else:
            print (userlogin.errors, userregister.errors)





    else:
        userlogin = LoginForm()
        userregister = RegisterationForm()
    return render(request,'signup.html', {'userlogin': userlogin, 'userregister': userregister})



def user_logout(request):
    logout(request)
    return redirect('registration')

