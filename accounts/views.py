from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
 if request.method=='POST':
  username=request.POST['username']
  email=request.POST['email']
  passwd=request.POST['password']
  confPasswd=request.POST['confirmpassword']
  if passwd==confPasswd:
   if User.objects.filter(username=username).exists():
    messages.warning(request,"username already exists")
    return redirect ('signup')
   
   if User.objects.filter(email=email).exists():
    messages.warning(request,"Email already exists")
    return redirect ('signup')
   else:
    userData=User(username=username,email=email,password=passwd)
    userData.save()
    messages.success(request,'Successfully Registered')
    return redirect ('login')
  else:
   messages.warning(request,"Password do not match")
   return redirect("signup")
 return render (request,'webpages/signup.html')

def login(request):
 if request.method=='POST':
  username=request.POST['username']
  passwd=request.POST['password']
  user=auth.authenticate(username=username,password=passwd)
  if user is not None:
   auth.login(request,user)
   messages.success(request,'Login is successful')
   return redirect('dashboard')
  else:
   messages.error(request,'Username or password is wrong')
   return redirect('login')
 return render (request,'webpages/login.html')

@login_required()
def logout_user(request):
 auth.logout(request)
 return redirect('login')

@login_required(login_url='login')
def dashboard(request):
 return render(request,'accounts/dashboard.html')