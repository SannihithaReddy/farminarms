from django.shortcuts import redirect, render
import requests
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

        obj = location(name=cname,soilt=soilt,temp=temp,humd=humd,desc=desc,cust=request.user)
        obj.save()

        #dest=crop.objects.raw('select * from crop where cmintemp<temp and cmaxtemp>temp;')[0]

        dest = crop.objects.filter(Q(cmintemp__lte = temp) & Q(cmaxtemp__gte = temp))
        print(dest)
        #return redirect('/weather/suggest/')
        return render(request,'getdet.html',{'data':dest})
    else:
        return render(request,'getdet.html')


def suggest(request):
    return render(request, 'suggest.html')

def rice(request):
    return render(request, 'rice.html')

def dispwea(request):
    return render(request, 'dispwea.html')
