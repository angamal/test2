from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method=='POST':
     Username = request.POST.get('username')
     first_name = request.POST.get('first_name')
     last_name=request.POST.get('last_name')
     email = request.POST.get('email')
     Password = request.POST['Password']
     Cpassword = request.POST.get('Cpassword')
     if Password == Cpassword:
         if User.objects.filter(username=Username).exists():
            messages.info(request,"username Taken")
            return redirect('register')
         elif User.objects.filter(email=email).exists():
           messages.info(request,"email Taken")
           return redirect('register')
         else:
            user=User.objects.create_user(username = Username,password = Password,first_name = first_name,last_name = last_name,email = email)
            user.save()
            return redirect('login')
     else:
        messages.info(request,"password not matching")
        return redirect('register')
     return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')




