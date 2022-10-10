from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customers,CustomersForm, EditCustomersForm
from django.core.paginator import Paginator
from django.http.response import HttpResponse
# Create your views here.

class ProductsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Products"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-products.html',greeting)

class ProductDetailView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Product Detail"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-productdetail.html',greeting)       

class OrdersView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Orders"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-orders.html',greeting)          

class CustomersView(LoginRequiredMixin,View):
    def get(self , request):
        form = CustomersForm()
        customers_record = Customers.objects.all()
        p = Paginator(customers_record, 8)
        page = request.GET.get('page')
        if p == None:
            page = int(1)
        page_obj = p.get_page(page)
        greeting = {}
        greeting['heading'] = "Customers"
        greeting['pageview'] = "Ecommerce"
        greeting['page_obj'] = page_obj
        greeting['form'] = form
        greeting['form1'] = EditCustomersForm()
        return render (request,'ecommerce/ecommerce-customers.html',greeting)      
    def post(self, request):
        if request.method == "POST":
            if "addcustomer" in request.POST:
                form = CustomersForm(request.POST)
                form.save()
                page_number = request.POST['page_number']
                return redirect("/ecommerce/customers" + "?page="+str(page_number))
            if "editcustomer" in request.POST:
                id = request.POST['id']
                username = request.POST['username']
                email = request.POST['email']
                phone = request.POST['phone']
                rating = request.POST['rating']
                wallet_balance = request.POST['wallet_balance']
                address = request.POST['address']
                page_number = request.POST['page_number']

                user = Customers.objects.filter(id=id).update(username=username,email=email,phone=phone,rating=rating,wallet_balance=wallet_balance,address=address)
                return redirect("/ecommerce/customers" + "?page="+str(page_number))
            if "deleteCustomer" in request.POST:
                id = request.POST['id']
                obj = Customers.objects.filter(id=id).first()
                obj.delete()
                return HttpResponse()
# Edit Customer
class CartView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Cart"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-cart.html',greeting)      

class CheckOutView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Checkout"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-checkout.html',greeting) 

class ShopsView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Shops"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-shops.html',greeting)                                         

class AddProductView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Add Product"
        greeting['pageview'] = "Ecommerce"
        return render (request,'ecommerce/ecommerce-addproduct.html',greeting)                                                 