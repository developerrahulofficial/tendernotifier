from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
# Create your views here.

class StarterPageView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Starter Page"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-starterpage.html',greeting)

class MaintainanceView(LoginRequiredMixin,View):
    def get(self , request):
        return render (request,'utility/utility-maintainance.html')  

class ComingSoonView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'utility/utility-comingsoon.html')              

class TimeLineView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Timeline"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-timeline.html',greeting) 

class FaqView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "FAQs"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-faq.html',greeting)  

class PricingView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Pricing"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-pricing.html',greeting)                       

class ErrorPageView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'utility/utility-404error.html')    

class ErrorPageExtraView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'utility/utility-500error.html')


# Authentication
class AuthLoginView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-login.html')
        
class AuthRegisterView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-register.html')
class AuthRecoverpwView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-recoverpw.html')
class AuthLockScreenView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-lock-screen.html')
class AuthChangePasswordView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-password-change.html')
class AuthConfirmMailView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-confirm-mail.html')
class AuthEmailVerificationView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-email-verification.html') 
class AuthTwoStepVerificationView(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-two-step-verification.html')  


#Viewscreen 2
class AuthLogin2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-login-2.html')
class AuthRegister2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-register-2.html')
class AuthRecoverpw2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-recoverpw-2.html')
class AuthLockScreen2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-lock-screen-2.html')
class AuthChangePassword2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-password-change-2.html')
class AuthConfirmMail2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-confirm-mail-2.html')
class AuthEmailVerification2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-email-verification-2.html')   
class AuthTwoStepVerification2View(LoginRequiredMixin,View):
    def get(self , request):    
        return render (request,'authentication/auth-two-step-verification-2.html')  
