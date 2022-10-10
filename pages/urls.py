from django.urls import path
from pages import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView)
urlpatterns = [
    path('starterpage',views.StarterPageView.as_view(),name='utility-starterpage'),
    path('maintainance',views.MaintainanceView.as_view(),name='utility-maintainance'),
    path('comingsoon',views.ComingSoonView.as_view(),name='utility-comingsoon'),
    path('timeline',views.TimeLineView.as_view(),name='utility-timeline'),
    path('faq',views.FaqView.as_view(),name='utility-faq'),
    path('pricing',views.PricingView.as_view(),name='utility-pricing'),
    path('404error',views.ErrorPageView.as_view(),name='utility-404error'),
    path('500error',views.ErrorPageExtraView.as_view(),name='utility-500error'),



    # Authentication
    #Viewscreen 1
    path('auth-login',views.AuthLoginView.as_view(),name ='authlogin'),
    path('auth-register',views.AuthRegisterView.as_view(),name ='authregister'),
    path('auth-lock-screen',views.AuthLockScreenView.as_view(),name ='authlockscreen'),
    path('auth-authrecoverpw',views.AuthRecoverpwView.as_view(),name ='authrecoverpw'),
    path('auth-change-password',views.AuthChangePasswordView.as_view(),name ='passwordchange'),
    path('auth-confirm-mail',views.AuthConfirmMailView.as_view(),name ='confirmmail'),
    path('auth-email-verificaton',views.AuthEmailVerificationView.as_view(),name ='emailverificaton'),
    path('auth-two-step-verificaton',views.AuthTwoStepVerificationView.as_view(),name ='twostepverification'),
    #Viewscreen 2
    path('auth-login-2',views.AuthLogin2View.as_view(),name ='authlogin2'),
    path('auth-register-2',views.AuthRegister2View.as_view(),name ='authlregister2'),
    path('auth-recoverpw-2',views.AuthRecoverpw2View.as_view(),name ='authrecoverpw2'),
    path('auth-lock-screen-2',views.AuthLockScreen2View.as_view(),name ='authlockscreen2'),
    path('auth-change-password-2',views.AuthChangePassword2View.as_view(),name ='passwordchange2'),
    path('auth-confirm-mail-2',views.AuthConfirmMail2View.as_view(),name ='confirmmail2'),
    path('auth-email-verificaton-2',views.AuthEmailVerification2View.as_view(),name ='emailverificaton2'),
    path('auth-two-step-verificaton-2',views.AuthTwoStepVerification2View.as_view(),name ='twostepverification2'),
    
]

