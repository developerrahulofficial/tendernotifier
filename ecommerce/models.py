from django.db import models
from django import forms
from django.forms.widgets import TextInput
# Create your models here.

rating_choice = [
    (0,'Select'),
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5')
]

class Customers(models.Model):
    username = models.CharField(max_length=96)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=96)
    address = models.CharField(max_length=500)
    rating = models.PositiveSmallIntegerField(choices=rating_choice)
    wallet_balance = models.IntegerField()
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username + " | " + str(self.joining_date)

class CustomersForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Address'}))
    wallet_balance = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Wallet Balance'}))
    rating = forms.CharField(widget=forms.Select(choices=rating_choice,attrs={'placeholder':'Rating'}))
    class Meta:
        model = Customers
        fields = ["username","phone","email","address","rating","wallet_balance"]
class EditCustomersForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username','placeholder':'Username'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'id':'phone','placeholder':'Phone'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'email','placeholder':'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'id':'address','placeholder':'Address'}))
    wallet_balance = forms.IntegerField(widget=forms.TextInput(attrs={'id':'wallet_balance','placeholder':'Wallet Balance'}))
    rating = forms.CharField(widget=forms.Select(choices=rating_choice,attrs={'id':'rating','placeholder':'Rating'}))
    class Meta:
        model = Customers
        fields = ["username","phone","email","address","rating","wallet_balance"]