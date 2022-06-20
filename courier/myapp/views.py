from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CourierForm
from .models import CourierService



# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        # user name =request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"your account has been successfully completed")

        return redirect('signin')


    return render(request,'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'create.html',{'fname':fname})
        else:
            messages.error(request,'bad credentials!')
            return redirect('home')

    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,'logout successfully!')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form =CourierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
        form=CourierForm()
    return render(request,'create.html',{'form':form})
