from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def account(request):
    return render(request,'account.html')
def login(request):
    return render(request,'login.html')

    
def dashboard(request):
    return render(request,'dashboard.html')




def signup(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user =User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name, email=email)
        print("users created")
        return redirect('/account')
    else:
            return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
         auth.login(request, user)
         print("user is logged in")
         return redirect('/account/dashboard')
         
    else:
            return render(request, 'login.html')

