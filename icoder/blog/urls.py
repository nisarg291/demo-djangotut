from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('blog',views.blog,name='blog')
]