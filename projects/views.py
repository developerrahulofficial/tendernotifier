from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ProjectsGridView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Projects Grid"
        greeting['pageview'] = "Projects"
        return render (request,'projects/projectsgrid.html',greeting)

class ProjectsListView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Projects List"
        greeting['pageview'] = "Projects"
        return render (request,'projects/projectslist.html',greeting)

class ProjectOverviewView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Project Overview"
        greeting['pageview'] = "Projects"
        return render (request,'projects/projectsoverview.html',greeting)

class CreateViewView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Create New Project"
        greeting['pageview'] = "Projects"
        return render (request,'projects/createnew.html',greeting)
