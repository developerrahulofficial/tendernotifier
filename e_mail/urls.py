from django.urls import path
from e_mail import views

urlpatterns = [
    #email
    path('inbox',views.InboxView.as_view(),name='email-inbox'),
    path('reademail',views.ReadEmailView.as_view(),name='email-reademail'),
    path('templates/basicaction',views.BasicActionView.as_view(),name='email-templates-basicaction'),
    path('templates/alertemail',views.AlertEmailView.as_view(),name='email-templates-alertemail'),
    path('templates/billingemail',views.BillingEmailView.as_view(),name='email-templates-billingemail'),

]