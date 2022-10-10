"""skote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from skote import views
from .views import MyPasswordSetView ,MyPasswordChangeView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
urlpatterns = [
    # my urls
    path('insert/', TemplateView.as_view(template_name="form.html")),
    # tender settings
    path('tender-setting',views.tender_settings,name="tender_settings"),
    path('save-tender-settings',views.save_tender_settings,name="save_tender_settings"),
    path('search/',views.search_address,name='search'),
    path('scraper',views.Scraper,name="scraper"),

    path('insert/home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    # Dashboards View
    # path('',views.DashboardView.as_view(),name='dashboard'),
    path('',views.SaasView.as_view(),name='dashboard'),
    path('dashboard_saas',views.SaasView.as_view(),name='dashboard_saas'),
    path('dashboard_crypto',views.CryptoView.as_view(),name='dashboard_crypto'),
    path('dashboard_blog',views.BlogView.as_view(),name='dashboard_blog'),
    # Calender View
    path('calendar',views.CalendarView.as_view(),name='calendar'),
    path('full-calendar',views.CalendarFullView.as_view(),name='full-calendar'),
    # Chat View
    path('chat',views.ChatView.as_view(),name='chat'),
    # Layouts
    path('layout/',include('layout.urls')),
    # File manager View
    path('filemanager',views.FileManagerView.as_view(),name='filemanager'),
    #Ecommerce
    path('ecommerce/',include("ecommerce.urls")),
    #Crypto
    path('crypto/',include('crypto.urls')),
    #Email
    path("email/",include("e_mail.urls")),
    #Invoices
    path('invoices/',include('invoices.urls')),
    #Projects
    path('projects/',include('projects.urls')),
    #Tasks
    path('tasks/',include('tasks.urls')),
    #Blog
    path('blog/',include('blog.urls')),
    #Blog
    path('contacts/',include('contacts.urls')),
    #Authencation
    # path('authentication/',include('authentication.urls')),
    #Pages
    path('pages/',include('pages.urls')),
    #Components
    path('components/',include('components.urls')),
    # Allauth
    path('account/', include('allauth.urls')),
    path('auth-logout/',TemplateView.as_view(template_name="account/logout-success.html"),name ='pages-logout'),
    path('auth-lockscreen/',TemplateView.as_view(template_name="account/lock-screen.html"),name ='pages-lockscreen'),
        #Custum change password done page redirect
    path('accounts/password/change/', login_required(MyPasswordChangeView.as_view()), name="account_change_password"),
    #Custum set password done page redirect
    path('accounts/password/set/', login_required(MyPasswordSetView.as_view()), name="account_set_password"),
]

