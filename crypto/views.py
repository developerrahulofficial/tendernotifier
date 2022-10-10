from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class WalletView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Wallet"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-wallet.html',greeting)

class BuySellView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Buy/Sell"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-buysell.html',greeting)

class ExchangeView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Exchange"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-exchange.html',greeting)

class LendingView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Lending"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-lending.html',greeting)        

class OrdersView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Orders"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-orders.html',greeting)  

class KYCView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "KYC Application"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-kycappication.html',greeting)  

class ICOLandingView(LoginRequiredMixin,View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "ICO Landing"
        greeting['pageview'] = "Crypto"
        return render (request,'crypto/crypto-icolanding.html',greeting)                         