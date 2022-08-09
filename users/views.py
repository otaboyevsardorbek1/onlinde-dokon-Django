from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login

from .forms import UserLoginForm, UserRegisterForm

def user_form_view(request):
    return render(request, "users/user_form.html")

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password =  request.POST['password']
            user = authenticate(username=username, password=password)
            user.is_authenticated
            
            if user and user.is_active:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    context ={
        'form': form,
    }
    return render(request, 'users/user_login.html', context)
    
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            print(form.save())
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context ={
        'form': form,
    }
    return render(request, 'users/user_register.html', context)
    
    
    
                
