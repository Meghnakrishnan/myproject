from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # Default route for app1,
    path('',views.index,name='index'),
    
]