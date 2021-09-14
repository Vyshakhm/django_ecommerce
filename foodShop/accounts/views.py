from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username= request.POST['username']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
        else:
            messages.info(request,'password mismatch!')
            print('mismatch')
            return redirect('register')
        return redirect('login')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('logged')
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')