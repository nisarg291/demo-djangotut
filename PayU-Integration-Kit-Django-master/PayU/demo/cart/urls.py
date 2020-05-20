# from django.conf.urls import patterns, include, url
# from . import views
#
# urlpatterns = patterns('',
#     url('checkout/', views.checkout, name='order.checkout'),
#     url('success/', views.success, name='order.success'),
#     url('failure/', views.failure, name='order.failure'),
#     url('cancel/', views.cancel, name='order.cancel'),
# )
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='order.checkout'),
    path('success/', views.success, name='order.success'),
    path('failure/', views.failure, name='order.failure'),
    path('cancel/', views.cancel, name='order.cancel'),
]
