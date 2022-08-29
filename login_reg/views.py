from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import RegisterUserForm, EditUserForm, EditPasswordForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            context = {'user': user}
            return redirect('tracker/home', context)
        else:
            messages.success(request, ('There was a problem logging in'))
            return redirect('/')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'authenticate/login_reg.html', context)

def logout_user(request):
    messages.success(request, ('You have been logged out'))
    logout(request)
    return redirect('/')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('tracker/home')
        else:
            messages.success(request, ('There was a problem with your form'))
            context = {'form': form }
            return render(request, 'authenticate/login_reg.html', context)

    else:
        form = RegisterUserForm()
        context = {'form': form }
        return render(request, 'authenticate/login_reg.html', context)

def edit_profile(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, ('Your profile has been updated'))
            form.save()
            return redirect('/edit_profile')
        else:
            messages.success(request, ('There was a problem with your form'))
            context = {'form': form}
            return render(request, 'authenticate/edit_profile.html', context)
    else:
        form = EditUserForm(instance=request.user)
        context = {'form': form}
        return render(request, 'authenticate/edit_profile.html', context)

def edit_password(request):
    if request.method == "POST":
        form = EditPasswordForm(request.user, request.POST)
        if form.is_valid():
            messages.success(request, ('Your password has been updated'))
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("/edit_profile")
        else:
            messages.success(request, ('There was a problem with your form'))
            context = {'form': form}
            return render(request, "authenticate/password.html", context)
    else:
        form = EditPasswordForm(request.user)
        context = {'form': form}
        return render(request, 'authenticate/password.html', context)


# Create your views here.
