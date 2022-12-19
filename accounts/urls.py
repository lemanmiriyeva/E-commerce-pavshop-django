from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  (Logout, register, loginView, ActivateAccountView)


urlpatterns = [ 
    path('login/', loginView.as_view(), name = 'login'),
    path('register/', register.as_view(), name ='register' ),
    path('activate/<str:uidb64>/<str:token>/', ActivateAccountView.as_view(), name ='activate' ),
    path('logout/', Logout.as_view() , name='logout'),
     path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password/password_reset.html',
             subject_template_name='password/password_reset_subject.txt',
             email_template_name='password/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password/password_reset_complete.html'
         ),
         name='password_reset_complete'),
     path('change_password/',auth_views.PasswordChangeView.as_view(template_name='password/change_password.html',success_url = '/'),name='change_password'
    ),

]
   