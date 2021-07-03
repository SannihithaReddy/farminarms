from django.shortcuts import redirect, render
import requests
from requests.api import request
from .models import crop, location
from django.db.models import Q
#from accounts.models import User


# Create your views here.
def det(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        zcode = request.POST['zcode']
        soilt = request.POST['soiltype']
        api_key = "8d7fc4b01819676b788ed6f1048470bd"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        curl=base_url + 'zip='+ str(zcode) +','+'in' + '&appid=' + api_key
        

        response = requests.get(curl)
        x = response.json()
        if x["cod"] != "404":

	        y = x["main"]
	        temp = y["temp"]-273     #Degree Centigrade
	        humd = y["humidity"]     #percentage

	        z = x["weather"]
	        desc = z[0]["description"]

        obj = location(name=cname,soilt=soilt,temp=temp,humd=humd,zipcode=zcode,desc=desc,cust=request.user)
        obj.save()

        #qry="select * from weather_crop where cmintemp< %s and cmaxtemp> %s" %(temp,temp)
        #dest=crop.objects.raw(qry)
        #dest=crop.objects.raw('select * from crop where cmintemp<temp and cmaxtemp>temp;')[0]

        dest = crop.objects.filter(Q(cmintemp__lte = temp) & Q(cmaxtemp__gte = temp) &
         Q(cminhum__lte = humd) & Q(cmaxhum__gte = humd) & Q(csoiltype = soilt))
        #print(dest)
        #return redirect('/weather/suggest/')
        return render(request,'dispcrop.html',{'dest':dest})
    else:
        return render(request,'getdet.html')


def suggest(request):
    return render(request, 'suggest.html')


def dispcrop(request):
    return render(request, 'dispcrop.html')


def dispwea(request):
    if request.method == 'POST':
        zcode = request.POST['zcode']
        api_key = "8d7fc4b01819676b788ed6f1048470bd"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        curl=base_url + 'zip='+ str(zcode) +','+'in' + '&appid=' + api_key
        
        response = requests.get(curl)
        x = response.json()
        if x["cod"]!="404":
            y=x["main"]

            temp = y["temp"] - 273
            pres = y["pressure"]
            humd = y["humidity"]

            z = x["weather"]
            desc = z[0]["description"]
        return render(request,'dispwea.html',{'t':"Temperature (in Degree Centigrade) = ",'temp':temp,
        'p':"atmospheric pressure (in hPa unit) = ",'pres':pres,'h':"humidity (in percentage) = ",'humd':humd,
        'd':"Weather Description :",'desc':desc})

    else:
        return render(request,'dispwea.html')

def rice(request):
    return render(request, 'rice.html')

def maize(request):
    return render(request, 'maize.html')

def scane(request):
    return render(request, 'scane.html')

def bgram(request):
    return render(request, 'bgram.html')

def gnut(request):
    return render(request, 'gnut.html')

def chilli(request):
    return render(request, 'chilli.html')

def cotton(request):
    return render(request, 'cotton.html')

def sbean(request):
    return render(request,'sbean.html')

def mgmt(request):
    return render(request,'crop_mgmt.html')
