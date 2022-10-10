from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserGridView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "User Grid"
        greeting['pageview'] = "Contacts"
        return render (request,'contacts/usergrid.html',greeting)

class UserListView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "User List"
        greeting['pageview'] = "Contacts"
        return render (request,'contacts/userlist.html',greeting)

class ProfileView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Profile"
        greeting['pageview'] = "Contacts"
        return render (request,'contacts/profile.html',greeting)