from django.shortcuts import redirect, render
from user.forms import EmailAuthenticationForm, UserRegistrationForm
from user.models import *
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'user/dashboard.html')

class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'user/signup.html',{'form':form})
    
    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulation! Your account has been created Successfully.")
            email=request.POST['email']
            username=email.split('@')[0]
            password=request.POST['password1']
            reg = User(username=username,email=email,password=password)
            reg.save()
        return render(request,'user/signup.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = EmailAuthenticationForm(request)
    return render(request, 'user/signin.html', {'form': form})

