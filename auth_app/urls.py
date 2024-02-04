from django.urls import path,include
from auth_app import views

urlpatterns = [
    #SECTION - ===========================create account and login =========================================
    path('singup/',views.singupview.as_view(),name='singup_view'),

    path('',views.signinView.as_view(),name='signin_View'),
    
    path('signout/', views.SignOutView.as_view(), name='signout_view'),
    
    #SECTION - <<<<<<<<<<<<<<<<<<<<<<<<Password  reset section>>>>>>>>>>>>>>>>>>>>>>>>
    path('password/reset/',views.Prview.as_view(),name='password_reset'),
    
    path('password/reset/done/',views.Prdone.as_view(),name='password_reset_done'),
    
    path('password/reset/confirm/<uidb64>/<token>',views.Prconfirm.as_view(),name='password_reset_confirm'),
    
    path('password/reset/complete',views.Prcomplete.as_view(),name='password_reset_complete'),
    
    
    #SECTION -  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Change Password on profile>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    path('change_password/',views.change_password.as_view(),name='change_password'),
    
    path('change_password_done',views.change_password_done.as_view(),name='change_password_done'),

]