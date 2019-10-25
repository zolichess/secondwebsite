from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse('<h1>Wellcome</h1>')

def about_view(request):
    return HttpResponse('<h1>about</h1>')

def contact_view(request):
    return HttpResponse('<h1>contact</h1>')


