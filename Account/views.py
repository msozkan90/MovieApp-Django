from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.
def sign_in(request):
    form=AuthenticationForm()
    if request.method== "POST":
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in succesfully')
                return redirect('moviess:index')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context={"form":form}
    return render(request,"signin.html",context)

def sign_out(request):
    logout(request)
    messages.success(request, "You are logged out succesfully")
    return redirect('moviess:index')

def register(request):
        form=CreateUserForm()
        if request.method=="POST":
                form=CreateUserForm(request.POST)
                if form.is_valid:
                    user = form.save(commit=False)
                    user.save()
                    messages.success(request,"You are registered successfully")
                    return redirect("account:sign_in")
        return render(request,"register.html",{"form":form})