from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from .forms import SignUp, Login
from cryptography.fernet import Fernet
# Create your views here.

def redirect(response):
    return HttpResponseRedirect('/register/signup/')

def sign_up(response):
    if response.method == 'POST':
        form = SignUp(response.POST)
        if form.is_valid():
            key = Fernet.generate_key()
            fernet = Fernet(key)
            user = form.cleaned_data['usern']
            email = form.cleaned_data['email']
            passw = form.cleaned_data['passw']

            try:
                User.objects.get(username=user) 
                print("USER ALREADY EXISTS SO SIGNUP ABANDONED!")
            except User.DoesNotExist:
                try:
                    User.objects.get(email=email)
                    print("User with that email already exists!")
                except User.DoesNotExist:
                    # we are good to go!
                    print(f'user: {user}; email: {email}; passw: {passw}')
                    user_ = User(username=user, email=email,
                    password=fernet.encrypt(passw.encode()).decode(), key=key.decode())
                    user_.save()

            
        else:
            print(form.errors)

    return render(response, 'register/signup.html', {})

def login(response):
    if response.method == 'POST':
        form = Login(response.POST)
        if form.is_valid():
            username = form.cleaned_data['usern']
            password = form.cleaned_data['passw']

            try:
                user = User.objects.get(username=username)
                fernet = Fernet(user.key.encode())
                if fernet.decrypt(user.password.encode()).decode() == password:
                    print("Login Credentials are correct!") #* LOGIN SUCCESSFUL
                    return HttpResponseRedirect('/')
                else:
                    print(fernet.decrypt(user.password.encode()))
                    print("Login Credentials are incorrect") #! LOGIN FALID
            except User.DoesNotExist:
                print("User not found!")

    return render(response, 'register/login.html', {})