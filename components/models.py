from django.db import models

# Create your models here.
from django.db import models

class Bids(models.Model):
    Bid_number= models.CharField(max_length=100)
    Department_Name = models.CharField(max_length=100)
    Address=models.CharField(max_length=100,null=True)
    Services=models.CharField(max_length=300)
    Start_date=models.DateField()
    Start_time=models.CharField(max_length=100)
    End_date=models.DateField()
    End_time=models.CharField(max_length=100)
    PdfLink=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Particiaped=models.BooleanField(default=False)

class Userdata(models.Model):
    User=models.CharField(max_length=100)
    Services=models.CharField(max_length=1000)
    Locations=models.CharField(max_length=1000)




