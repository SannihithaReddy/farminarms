
from django.db import models
from accounts.models import User

# Create your models here.
class location(models.Model):
    name = models.CharField(max_length=20, null=False)
    temp = models.FloatField(null=True)
    soilt = models.CharField(max_length=20,null=True)
    humd = models.FloatField(null=True)
    desc = models.CharField(max_length=50,null=True)
    precip = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)

    cust = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.name


class crop(models.Model):
    cname=models.CharField(max_length=30,null=False)
    cimg=models.ImageField(upload_to='pics')
    cmintemp=models.FloatField(null=True,blank= True)
    cmaxtemp=models.FloatField(null=True,blank= True)
    cminhum=models.FloatField(null=True,blank= True)
    cmaxhum=models.FloatField(null=True,blank= True)
    cminprecip=models.FloatField(null=True,blank= True)
    cmaxprecip=models.FloatField(null=True,blank= True)
    csoiltype=models.CharField(max_length=30,null=True,blank= True)

    croploc=models.ManyToManyField(location,blank=True)

    def __str__(self):
        return self.cname