from django.conf import settings
from django.contrib.auth import login
from . import forms
import requests
from django.shortcuts import redirect,render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Signup(View):

    def get(self,request):
        form = forms.SignupForm()
        return render(request,'new/signup.html',context={'form':form})

    def post(self,request):
        form= forms.SignupForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)

@login_required()
def ninde(request):
      response= requests.get('https://ipwho.is/fields= ip,timezone.current_time,country,flag.emoji')
      return render(request,'new/base1.html',{'response':response})


class Currencies(View):

    def get(self,request):
        url = 'https://currency-converter5.p.rapidapi.com/currency/list"'
        querystring = {"format":"json"}
        headers = {"X-RapidAPI-KEY": "29a64677b3msh3e760bd6bc4016ap1c0663jsne86061996f08",
                   "X-RapidAPI-Host":"currency-converter5.p.rapidapi.com"}
        response= requests.request("GET", url,headers=headers,params=querystring)
        return render(request, 'new/currencies.html',{'response':response})