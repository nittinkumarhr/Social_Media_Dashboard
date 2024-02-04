from django.db import models
from user.models import User
from crum import get_current_user

from core.utils import auto_save_current_user

# Create your models here.
#SECTION - <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Post models>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Post(models.Model):
    text_post=models.CharField(max_length=140,blank=True,null=True)
    
    image=models.ImageField(upload_to='post_images') # Base_dir => media => post_images
    
    user=models.ForeignKey(User,on_delete=models.PROTECT,editable=False)
    
    created_on=models.DateTimeField(auto_now_add=True)
    
    updated_on=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-created_on']
    
     # Function to return a string representation of the Post object
    def __str__(self):
        return f"Post {self.pk}"
    

    
    def save(self, *args, **kwargs):
        user = get_current_user()
        # If there is a current user and they don't have a primary key (i.e. they haven't been saved to the database yet),
        # then set the user to None
        if user and not user.pk:
            user = None
        # If this is a new Post (i.e. the primary key is None), then set the user to the current user
        if not self.pk:
            self.user = user

        # Call the parent class's save method to save the object to the database
        super(Post, self).save(*args, **kwargs)
        
    #SECTION - <<<<<<<<<<<<<<<<<<<<<<<<<< count the like and comment on the post>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    @property
    def likes_count(self):
        count = self.like_set.count()
        return count

    @property
    def comments_count(self):
        count = self.comment_set.count()
        return count

#SECTION - .....................................Comments Models...............................................

class Comment(models.Model):
    
    text_comment=models.CharField(max_length=240)
    
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    
    commented_on=models.DateTimeField(auto_now_add=True)
    
    updated_on=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text_comment
         # Function to return a string representation of the Post object

    
    def save(self, *args, **kwargs):    
        user = get_current_user()
        # If there is a current user and they don't have a primary key (i.e. they haven't been saved to the database yet),
        # then set the user to None
        if user and not user.pk:
            user = None
        # If this is a new Post (i.e. the primary key is None), then set the user to the current user
        if not self.pk:
            self.user = user

        # Call the parent class's save method to save the object to the database
        super(Comment, self).save(*args, **kwargs)
    
    
#SECTION -  ----------------------------------Like models------------------------------------------------------------  

class Like(models.Model):
    
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    
   
    
    liked_on=models.DateTimeField(auto_now_add=True)
    
    updated_on=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.Post.id)
    
         # Function to return a string representation of the Post object

    
    def save(self, *args, **kwargs):
        user = get_current_user()
        # If there is a current user and they don't have a primary key (i.e. they haven't been saved to the database yet),
        # then set the user to None
        if user and not user.pk:
            user = None
        # If this is a new Post (i.e. the primary key is None), then set the user to the current user
        if not self.pk:
            self.user = user

        # Call the parent class's save method to save the object to the database
        super(Like, self).save(*args, **kwargs)
    
    
#SECTION -  <<<<<<<<<<<<<<<<<<<<savem models>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class SavedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post.pk)

    def save(self, *args, **kwargs):
        auto_save_current_user(self)
        super(SavedPost, self).save(*args, **kwargs)



#SECTION -  ******************************************* Followers Models ***********************************************

class Follower(models.Model):
    
    user=models.ForeignKey(User,related_name='follow_follower',on_delete=models.CASCADE,editable=False)
    
    followed=models.ForeignKey(User,related_name='follow_followed',on_delete=models.CASCADE)
    
    followed_on=models.DateTimeField(auto_now_add=True)
    
    updated_on=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.user} ---> {self.followed}"
    
    
    # Function to return a string representation of the Post object
    # def __str__(self):
    #     return str(self.pk)

    
    def save(self, *args, **kwargs):
        user = get_current_user()
        # If there is a current user and they don't have a primary key (i.e. they haven't been saved to the database yet),
        # then set the user to None
        if user and not user.pk:
            user = None
        # If this is a new Post (i.e. the primary key is None), then set the user to the current user
        if not self.pk:
            self.user = user

        # Call the parent class's save method to save the object to the database
        super(Follower, self).save(*args, **kwargs)
    
    
    
    