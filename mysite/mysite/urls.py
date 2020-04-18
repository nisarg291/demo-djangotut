from django.contrib import admin
from django.urls import path
from . import views

# Code for video 6
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#
# ]

# Code for video 7
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyse', views.analyse, name='analyse'),


]