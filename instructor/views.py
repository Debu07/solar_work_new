from django.shortcuts import render,redirect
from landing.decorators import unauthenticated_user
from .forms import UserSignupForm
from django.contrib.auth.models import Group
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from videos.forms import CourseForm,LessonForm



# @allowed_users(allowed_roles=['admin','teacher'])
def home(request):
    return render(request,'instructor/home.html')


@unauthenticated_user
def signupteacher(request):
    form=UserSignupForm()
    if request.method =='POST':
        form=UserSignupForm(request.POST)
        if form.is_valid():
            teacher=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='teacher')
            teacher.groups.add(group)
            messages.success(request, username +", Your Account has been successfully created! Login To continue ")
            return redirect('landing:login')
    context={'form':form}
    return render(request,'instructor/register.html',context)
    
@login_required(login_url="landing:login")
def teacherProfile(request):
    return render(request,'instructor/instructor_profile.html')


# @allowed_users(allowed_roles=['admin','teacher'])

@login_required(login_url='landing:login')
def create_course(request):
    form=CourseForm()
    if request.method=='POST':
        form=CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing:profile')
    context={'form':form}
    return render(request,'instructor/create_course.html',context)

def edit_course():
    pass

def delete_course():
    pass

def view_course():
    pass