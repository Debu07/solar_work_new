from django.urls import path
from . import views

app_name="instructor"

urlpatterns=[
    path('',views.teacherProfile,name="home"),
    path('createcourse/',views.create_course,name="createcourse"),

   
]