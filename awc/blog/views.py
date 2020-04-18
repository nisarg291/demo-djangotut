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

# Create your views here.
from django.http import HttpResponse
from .models import BlogPost
def index(request):
    return render(request, 'blog/index.html')

def blogPost(request, id):
    post = BlogPost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogPost.html',
                  {'post':post})