from django.shortcuts import render,HttpResponse

# Create your views here.
def home(index):
    return HttpResponse('this is index')
def blog():
    return HttpResponse('this is blog')