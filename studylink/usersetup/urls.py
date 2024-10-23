from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logOutUser, name="logout"),
    path('profile/', views.editProfile, name='userProfile'),
    path('search/', views.searchUsers, name='userSearch'),
    path('profile/<str:username>/', views.profile, name='profile'),
]