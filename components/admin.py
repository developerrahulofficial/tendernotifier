from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bids, Userdata

admin.site.register(Bids)
admin.site.register(Userdata)