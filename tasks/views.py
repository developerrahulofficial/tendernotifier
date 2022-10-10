from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TaskListView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Task List"
        greeting['pageview'] = "Tasks"
        return render (request,'tasks/tasklist.html',greeting)

class KanbanBoardView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Kanban Board"
        greeting['pageview'] = "Tasks"
        return render (request,'tasks/kanbanboard.html',greeting)

class CreateTaskView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Create Task"
        greeting['pageview'] = "Tasks"
        return render (request,'tasks/createtask.html',greeting)