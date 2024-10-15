from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def home(request):
    users = User.objects.all()
    return render(request, "myapp/home.html", {'users': users})
