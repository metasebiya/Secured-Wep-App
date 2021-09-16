from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .user_form import UserRegisterForm
from django.contrib.auth import login as dj_login
from feedback.views import IndexView


def index(request):
    return render(request, 'index.html')


def signup(request):
    return render(request, "signup.html")


# view for rendering login page
def login(request):
    return render(request, "login.html")


def signup_request(request):
    if request.method == 'POST':
        # get the post parameters
        uname = request.POST["uname"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        # check for errors in input
        if request.method == 'POST':
            try:
                user_exists = User.objects.get(username=request.POST['uname'])
                messages.error(
                    request, " Username already taken, Try something else!!!")
                return redirect("/signup")
            except User.DoesNotExist:
                if not firstName.isalnum():
                    messages.error(
                        request, " First name should only contain letters and numbers, Please try again")
                    return redirect("/signup")
                if not lastName.isalnum():
                    messages.error(
                        request, " Last name should only contain letters and numbers, Please try again")
                    return redirect("/signup")
                if len(uname) > 15:
                    messages.error(
                        request, " Username must be max 15 characters, Please try again")
                    return redirect("/signup")
                if not uname.isalnum():
                    messages.error(
                        request, " Username should only contain letters and numbers, Please try again")
                    return redirect("/signup")
                if password1 != password2:
                    messages.error(
                        request, " Password do not match, Please try again")
                    return redirect("/signup")
        # create the user
        user = User.objects.create_user(uname, email, password1)
        user.save()
        messages.success(
            request, " Your account has been successfully created")
        return redirect("/login")
    else:
        return HttpResponse('404 - NOT FOUND ')


def login_request(request):
    if request.method == 'POST':
        # get the post parameters
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        # cheching for valid login
        if user is not None:
            dj_login(request, user)
            messages.success(request, " Successfully logged in")
            return redirect("/dash")
        else:
            messages.error(request, " Invalid Credentials, Please try again")
            return redirect("/")
    return HttpResponse('404 - NOT FOUND ')


# view for rendering logout
def logout_request(request):
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')
