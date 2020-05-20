from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('this is index')
def contact(request):
    return HttpResponse('this is blog')
def about(request):
    return HttpResponse('this is blog')