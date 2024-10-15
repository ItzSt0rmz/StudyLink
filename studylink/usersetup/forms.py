from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class ClassesTakenForm(forms.ModelForm):

    # classes taken
    english1Taken = forms.BooleanField()
    english2Taken = forms.BooleanField()
    english3Taken = forms.BooleanField()
    english4Taken = forms.BooleanField()
    APlitTaken = forms.BooleanField()
    APlangTaken = forms.BooleanField()

    preAlgebraTaken = forms.BooleanField()
    algebra1Taken = forms.BooleanField()
    algebra2Taken = forms.BooleanField()
    geometryTaken = forms.BooleanField()
    preCalculusTaken = forms.BooleanField()
    calculusABTaken = forms.BooleanField()
    calculusBCTaken = forms.BooleanField()

    APphysics1Taken = forms.BooleanField()
    APphysicsCTaken = forms.BooleanField()
    chemTaken = forms.BooleanField()
    APchemTaken = forms.BooleanField()
    bioTaken = forms.BooleanField()
    APbioTaken = forms.BooleanField()
    APESTaken = forms.BooleanField()
    APpsychTaken = forms.BooleanField()

    class Meta:
        model = Profile