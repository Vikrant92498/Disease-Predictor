from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def forgotPassword(request):
    return render(request,'forgotpassword.html')
def changePassword(request):
    return render(request,'changepassword.html')