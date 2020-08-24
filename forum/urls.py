from django.urls import path
from . import views

app_name='forum'

urlpatterns = [
        path('',views.index,name="index"),
        path('thread/<int:thread_id>',views.thread,name="thread"),
        path('newthread/',views.new_thread,name="newthread"),

]
