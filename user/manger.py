
from django.contrib.auth.models import BaseUserManager

from django.utils.translation import gettext_lazy 


class customUserManager(BaseUserManager):
    
     
    #NOTE - Custom user manager that allows creating users with only an email and password.
    
    def create_user(self,email,password,username,**extra_filds):
        
        #NOTE - Create and save a user with the given email, password, and username.
        
        if not email:
            
            raise ValueError(gettext_lazy('The Email must be set'))
        
        email=self.normalize_email(email)
        
        user=self.model(email=email,username=username,**extra_filds)
        
        user.set_password(password)
        
        user.save()
        
        return user
    
    
    def create_superuser(self,email,password,username,**extra_filds):
        
        #NOTE - Create and save a superuser with the given email, password, and username.
        
        extra_filds.setdefault('is_active',True)
        
        extra_filds.setdefault('is_staff',True)
        
        extra_filds.setdefault('is_superuser',True)
        
        
        if extra_filds.get('is_staff') is not True:
            
            raise ValueError(gettext_lazy('Superuser must be assigned to is_staff=True'))
        
        if extra_filds.get('is_superuser') is not True:
            
            raise ValueError(gettext_lazy('Superuser must be assigned to is_superuser=True'))

        return self.create_user(email,password,username,**extra_filds)