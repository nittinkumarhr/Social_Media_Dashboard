from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib.auth import  get_user_model
from user.forms import UserEditForm
from django.contrib import messages
from django.db.models import Q
from core.models import Follower

# Create your views here.


#SECTION -  <<<<<<<<<<<<<<<<<<<<Profile view>>>>>>>>>>>>>>>>>>>>>

User=get_user_model()

class profileView(View):
    
    template_name_anon='user/anonymous_profile.html'
    
    template_name_auth='user/authenticated_profile.html'
    
    def get(self, request, *args, **kwargs):
        
        # Your view logic here
        try:
        
            username=kwargs.get('username') #NOTE -  fetch the url  username 
            
            user=User.objects.get(username=username)
            
        except Exception as e:
            return HttpResponse('This User  does not exit ')
        
        
        
        
        if username == request.user.username:
            
            context={'user':user}
            
            return render(request, self.template_name_auth,context=context)
        else:
            #SECTION -  follow and Unfollow conditions 
            try:
                Follower.objects.get(user=request.user, followed=user)
                is_follows_this_user = True
            except Exception as e:
                is_follows_this_user = False
                    
            context = { 'user': user, 'is_follows_this_user': is_follows_this_user }
            return render(request, self.template_name_anon, context=context)
            
            
        
#SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Profile edit view >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
class ProfileEditView(View):
    
    form_class=UserEditForm
    
    template_name='user/profile_edit.html'
    
    def get(self, request, *args, **kwargs):
        
        username = kwargs.get('username')

        if username != request.user.username:#LINK -  Check the login user edit  his own profile or other users profile
            return HttpResponse('<h1>This page does not exist.</h1>')

        form = self.form_class(instance=request.user)
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Saved your details in a safe place.')
            return redirect('profileView', request.user.username)
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
            context = {'form': form}
            return render(request, self.template_name, context=context)
        
#SECTION -   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< all Profile  Serch view >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class all_profile_view(View):
    
    template_name='user/all_profiles.html'
    
    def get(self, request, *args, **kwargs):
        
        search_term =request.GET.get('query')
        
        if search_term:
            
            all_profiles = User.objects.filter(
                    Q(username__contains=search_term) | Q(full_name__contains=search_term)
                ).exclude(
                    username=request.user.username
                )
        
        else:
            all_profiles=User.objects.none()
            
        
        context={'all_profiles':all_profiles}
        
        
        return render(request, self.template_name,context=context)
    
    
    
    
    

        
        
        
    
            


