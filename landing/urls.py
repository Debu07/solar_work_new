from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name='landing'

urlpatterns = [
     path('',views.home,name="home"),
     path('terms/',views.terms,name="terms"),
     path('login/',views.loginUser,name="login"),
     path('signup/',views.signupUser,name="signup"),
     path('about/',views.about,name="about"),
     path('logout/',views.logoutUser,name="logout"),
     path('profile/',views.profile,name="profile"),


     path('password_reset/',
          auth_views.PasswordResetView.as_view(template_name='landing/password_reset.html',success_url=reverse_lazy('landing:password_reset_done')),
               name="password_reset"),

     path('password_reset_sent/',
          auth_views.PasswordResetDoneView.as_view(template_name='landing/password_reset_sent.html'),
          name="password_reset_done"),

     path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name='landing/password_reset_form.html',success_url=reverse_lazy('landing:password_reset_complete')),
          name="password_reset_confirm"),

     path('password_reset_complete/',
          auth_views.PasswordResetCompleteView.as_view(template_name='landing/password_reset_done.html'),
          name="password_reset_complete"),

]
