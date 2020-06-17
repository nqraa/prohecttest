from django.urls import path, re_path
from .import views



urlpatterns = [
    path('',views.createprojectf),
    path('createproject/',views.createprojectf),

]