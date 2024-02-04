from django.db import models
from django.contrib.auth.models import AbstractUser # built i?n data base => built in table add the  column
from django.contrib.auth.base_user import BaseUserManager
from user.manger import customUserManager

GENDER_CHOICES=[
    ('M','Male'),
    ('F','Female'),
    ('F','Other'),
    ]
# Create your models here.


#SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<User model >>>>>>>>>>>>>>>>>>>>>
class User(AbstractUser):
    
    picture=models.ImageField(upload_to='Profile_pictures' ,null=True,blank=True)
    
    full_name=models.CharField(max_length=100)
    
    email=models.CharField(max_length=255,unique=True)
    
    first_name=None
    
    last_name=None
    
    #NOTE -  Optional filds
    
    
    bio=models.TextField(null=True,blank=True)
    
    website=models.URLField(null=True,blank=True)
    
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES,null=True,blank=True)
    
    is_private_account=models.BooleanField(null=True,blank=True)
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','username']
    
    objects=customUserManager()
    
    def __str__(self):
        return f"{self.id} - {self.name}"  # Adjust accordingly
    
#SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<<Count the follower and followeing>>>>>>>>>>>>>>>>>>>>>>>>
    
    
    #NOTE -   This property will be used to get the absolute url of user profile page
    
    
    
    @property
    def follower_count(self):
        count = self.follow_followed.count()
        return count
    
    def __str__(self):
        return self.email
    
    @property
    
    def following_count(self):
        
        count=self.follow_follower.count()
       
        return count
    
    @property
    
    def posts_count(self):
        count=self.post_set.count()
        
        return count
    
    