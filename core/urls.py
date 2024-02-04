#NOTE -  <<<<<<<<<<<<<<<<<<<<<< Core app >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from django.urls import path,include
from core import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('dashboard/',login_required(views.dashboard.as_view()),name='dashboard'),
    
    
    #SECTION - <<<<<<<<<<<<<<<<<<<<<<<<<< Follower and Following>>>>>>>>>>>>>>>>>>>>>>>
    
    path('follow/done/',login_required(views.FollowDoneView.as_view()),name='FollowDoneView'),
    
    path('unfollow/done/',login_required(views.UnFollowDoneView.as_view()),name='UnFollowDoneView'),
    
    #SECTION -<<<<<<<<<<<<<<<<<<<<Upload post>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('upload/post/',login_required(views.UploadPost.as_view()),name='UploadPost'),
    
    path('create/post',login_required(views.PostCreateView.as_view()),name='post_create_view'),
    
    #SECTION -  <<<<<<<<<<<<<<<<<<<Post Delete view >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('post/delete/<int:id>',login_required(views.post_delete_view.as_view()),name='post_delete_view'),
    
    #SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<go TO post Urls>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('post/<int:id>',login_required(views.PostDetailsView.as_view()),name='post_detail_view'),
    
    #SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<<<Post like and dislike >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('post/like/<int:id>/', views.PostLikeView.as_view(), name='post_like_view'),
    
    path('post/unlike/<int:id>/', views.PostUnlikeView.as_view(), name='post_unlike_view'),
    
    #SECTION -  <<<<<<<<<<<<<<<<<<<<<<<Post Comment View >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('post/comment/<int:id>/',views.PostCommentView.as_view(), name='post_comment_view'),

    
    #SECTION -  <<<<<<<<<<<<<<<<<<<<<<<Post SAve View >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('post/save/<int:id>/',views.PostsaveView.as_view(), name='post_save_view'),
    path('post/unsave/<int:id>/', login_required(views.PostUnsaveView.as_view()), name='post_unsave_view'),
    
    #SECTION - <<<<<<<<<<<<<<<<<<<Save post urls>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('post/saved/', login_required(views.SavedPostsView.as_view()), name='saved_posts_view'),
    
    #SECTION -  <<<<<<<<<<<<<<Explore Url>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    path('post/explore/', login_required(views.ExplorePostsView.as_view()), name='explore_posts_view'),
    
    #SECTION -  <<<<<<<<<<<<<<<<<<<<<<Liked view url >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('post/liked/', login_required(views.LikedPostsView.as_view()), name='liked_posts_view'),
    
    

    
    

]