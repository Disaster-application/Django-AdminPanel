from django.shortcuts import render, HttpResponse, redirect
from .models import admin_login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from .models import sendAlert
# Create your views here.
def login(request):

    data = admin_login()

    username = request.POST.get('username')
    user_pass = request.POST.get('user_password')
    print(f"Username: {username} \n Password: {user_pass}")
    email = "#"
    # user = User.objects.create_user(username='lol',password='lollogin',email=email)
    # user.save();
    store = list(User.objects.filter(username=username).values())
    if User.objects.filter(username=username).exists():
        print("Username exists")
        # print(make_password(user_pass))
        
        if check_password(user_pass,store[0]['password']):
            print("Log in Successfully")
            # return render(request, 'homepage.html')
            return redirect('/homepage')
        else:
            print("Incorrect Password")
            return redirect('/homepage')
        # return render(request, 'login.html')
    else:
        print("User dont Exists")
    return render(request, 'login.html')

def homepage(request):
    alertMsg = request.POST.get('alertMsg')
    alertType = request.POST.get('alertType')
    print(alertMsg,alertType)
    return render(request, 'homepage.html')
    # def redAlert():
    #     print("Danger Ahead")