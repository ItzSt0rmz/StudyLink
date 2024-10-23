from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UpdateUserForm, UpdateProfileForm, ClassesTakenForm

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated: 
        return redirect('home')
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, "users/register.html", context)

def loginPage(request):
    if request.user.is_authenticated: 
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "users/login.html", context)

@login_required(login_url='login')
def logOutUser(request):
    logout(request)
    return redirect('login')

@login_required
def editProfile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        classes_taken_form = ClassesTakenForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid() and classes_taken_form.is_valid():
            user_form.save()
            profile_form.save()
            classes_taken_form.save()

            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        classes_taken_form = ClassesTakenForm(request.POST, instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form, 'classes_form': classes_taken_form})

@login_required(login_url='login')
def searchUsers(request):
    return render(request, "users/user_search.html", {})

@login_required(login_url='login')
def profile(request, username=None):
      if username:
        profile_owner = get_object_or_404(User, username=username)

      else:
        profile_owner = request.user

      args1 = {
        'profile_owner': profile_owner,
      }
      
      return render(request, 'users/profile_view.html', args1)
