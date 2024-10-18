from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logOutUser, name="logout"),
    path('profile/', views.profile, name='userProfile'),
    path('search/', views.searchUsers, name='userSearch'),
]