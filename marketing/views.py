from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from marketing.models import Company
from django.core import serializers
from django.http import JsonResponse

def index(request):

    return render(request, 'index.html')


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('office')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('office')

            else:

                return redirect('sign_in')
        return render(request, 'sign_in.html')

def office(request):
    if request.user.is_authenticated:
        company = Company.objects.all()
        context={
            'company': company
        }
        return render(request, 'office-test.html', context)
    else:

        return redirect('sign_in')


