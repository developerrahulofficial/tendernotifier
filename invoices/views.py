from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class InvoiceListView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Invoice List"
        greeting['pageview'] = "Invoices"
        return render (request,'invoices/invoicelist.html',greeting)

class InvoiceDetailView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Invoice Detail"
        greeting['pageview'] = "Invoices"
        return render (request,'invoices/invoicedetail.html',greeting)        