#
# from django.http import HttpResponse
# from django.shortcuts import render
# from .models import BlogPost
# # Create your views here.
# def index(request):
#     return render(request,'blog/index.html');
# def blogpost(request, id):
#     post = BlogPost.objects.filter(post_id = id)[0]
#     print(post)
#     return render(request, 'blog/blogPost.html',{'post':post})
from django.shortcuts import render
from math import ceil
# Create your views here.
from django.http import HttpResponse
from .models import BlogPost

def index(request):
    myPosts=BlogPost.objects.all();
    return render(request, 'blog/index.html',{'myPosts': myPosts})

def blogPost(request, id):
    post = BlogPost.objects.filter(post_id = id)[0]
    max1=BlogPost.objects.all();


    if id <= 3:
        return render(request, 'blog/blogPost.html',
                      {'post': post,'next': int(id + 1),'max1':max1})
    elif id==9:
        return render(request, 'blog/blogPost.html',
                      {'post': post,'prev': int(id - 1),'max1':max1})
    else:
        return render(request, 'blog/blogPost.html',
                  {'post':post,'prev':int(id-1),'next':int(id+1),'max1':max1})
