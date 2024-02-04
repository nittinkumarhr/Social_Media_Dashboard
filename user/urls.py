#NOTE -  <<<<<<<<<<<<<<<<<<<<<< User app >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from django.urls import path,include
from user import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    
    path('in/<str:username>/',login_required(views.profileView.as_view()),name='profileView'),
    
    path('in/<str:username>/edit',login_required(views.ProfileEditView.as_view()),name='profile_edit_view'),
    
    path('in/profiles',login_required(views.all_profile_view.as_view()),name='all_profile_view'),


]