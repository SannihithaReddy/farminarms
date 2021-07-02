from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import User
#from .manager import UserManager

# Create your views here.
 

def register(request): 
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password1 = request.POST['upass']
        password2 = request.POST['cupass']
        phn = int(request.POST['phn'])
        if(password1 == password2):
            user = User.objects.create_user(first_name=first_name,last_name=last_name,password=password1,phn=phn)
            user.save()
            return redirect('/accounts/login/')
        else:
            print('passworn not matching.')
            return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        phn = request.POST['phn']
        password = request.POST['upass']

        user = auth.authenticate(phn=phn,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.Info(request,'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

