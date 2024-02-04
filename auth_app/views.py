from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import View
from auth_app.form import UserForm
from django.contrib.auth import authenticate, login,get_user_model,logout
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView
from django.contrib import messages 
from django.urls import reverse_lazy

# Create your views here.
#NOTE -  Class base view


User=get_user_model()
#SECTION -  -  ........................create account >>........................ 

class singupview(View):
    
    template_name='auth_app/signup.html'
    form_class=UserForm
    
    
    def get (self,request,*args, **kwargs):
        if request.user.is_authenticated: #NOTE -  check the user already login to return the dashboard or not return the login page
            return redirect('dashboard')
        
        return render(request,self.template_name)
    
    def post(self,request,*args, **kwargs):
        form=self.form_class(request.POST)
        # breakpoint()
        if form.is_valid():
            form.save()
            # breakpoint()
            return redirect('signin_View')
        context={'form':form}
        return render(request,self.template_name,context)
    
#SECTION -  - <<<<<<<<<<<<<<<<<<<<<<<<<< login Account>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class signinView(View):
    template_name='auth_app/signin.html'
    def get (self,request,*args, **kwargs):
        if request.user.is_authenticated: #NOTE -  check the user already login to return the dashboard or not return the login page
            return redirect('dashboard')
        return render(request,self.template_name)   
    # yaha per user login kerna ka logic
    def  post(self ,request,*args,**kwargs):
        email_username=request.POST.get('email_username')
        password= request.POST.get('password')
        
        
        try:
            user_obj=User.objects.get(username=email_username)
            email=user_obj.email
        except Exception as e :
            email=email_username
        
        user_auth=authenticate(request,email=email,password=password)
    
        if user_auth is  None:
            messages.error(request,'Invalid Login ...')
            return render(request,self.template_name,   )
        
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request,'Login Successfully ...')
            return redirect('dashboard')
        else:
            # Handle the case where authentication fails
            return redirect('signin_View')
        
        
#SECTION -  - <<<<<<<<<<<<<<<<<<<<<<<<<Logout view >>>>>>>>>>>>>>>>>>>>>
class SignOutView(View):
    def post(self, request, *args, **kwargs):
        # is user is not authenticated
        logout(request)
        return redirect('signin_View')





#SECTION - ......................Reset password .............................................


class Prview(PasswordResetView):
    subject_template_name='auth_app/password_reset_subject.txt'
    html_email_template_name= 'auth_app/password_reset_email.html'
    template_name='auth_app/password_reset.html'   
    
    
class Prconfirm(PasswordResetConfirmView):
    
    template_name='auth_app/password_reset_confirm.html'
    
class Prdone(PasswordResetDoneView):
    template_name='auth_app/password_reset_done.html'
    
class Prcomplete(PasswordResetCompleteView):
    template_name='auth_app/password_reset_complete.html'
    
    
#SECTION -  .......................user change password views.................

class change_password(PasswordChangeView):
    
    template_name='auth_app/password_change.html'
    
    success_url=reverse_lazy('change_password_done')
    
    
class change_password_done(PasswordChangeDoneView):
    
    template_name='auth_app/password_change_done.html'
    
    


