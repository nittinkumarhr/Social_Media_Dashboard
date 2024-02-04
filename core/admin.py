from django.contrib import admin
from .models import *

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    
    model=Post
    
    list_display=['text_post','image','user','created_on','updated_on']
    
admin.site.register(Post,PostModelAdmin)

#SECTION -  <<<<<<<<<<<<<<<<<<<< Comment  model >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class CommentModelAdmin(admin.ModelAdmin):
    
    model=Comment
    
    list_display=['text_comment','Post','user','commented_on','updated_on']
    

admin.site.register(Comment,CommentModelAdmin)


#SECTION -  <<<<<<<<<<<<<<<<<<<< Follow model >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class FollowModelAdmin(admin.ModelAdmin):
    
    model=Follower
    
    list_display=['followed','user','followed_on','updated_on']

admin.site.register(Follower,FollowModelAdmin)

#SECTION -  <<<<<<<<<<<<<<<<<<<<Like model >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class LikeModelAdmin(admin.ModelAdmin):
    
    model=Like
    
    list_display=['Post','user','liked_on','updated_on']



admin.site.register(Like,LikeModelAdmin)

#SECTION -  <<<<<<<<<<<<<<<<<<<<Save model >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class SavedPostModelAdmin(admin.ModelAdmin):
    model = SavedPost
    list_display = ('post', 'user', 'saved_on')
    
admin.site.register(SavedPost,SavedPostModelAdmin)





