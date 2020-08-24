from django.shortcuts import render , redirect
from .forms import UserSignupForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

def home(request):
    return render(request,'landing/body.html')

def terms(request):
    return render(request,'landing/terms.html')

def about(request):
    return render(request,'landing/about.html')

@unauthenticated_user
def loginUser(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('landing:home')
        else:
            messages.info(request,"Username or Password is incorrect")

    return render(request,'landing/login.html')


def logoutUser(request):
    logout(request)
    return redirect('landing:home')

@unauthenticated_user
def signupUser(request):
    form=UserSignupForm()
    if request.method == 'POST':
        form=UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request, username +", Your Account has been successfully created! Login To continue ")
            return redirect('landing:login')

    context={'form':form}
    return render(request,'landing/signup.html',context)

@login_required(login_url="landing:login")
def profile(request):
    return render(request,'landing/profile.html')




def change_password():
    pass

def edit_profile():
    pass