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
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class ClassesTakenForm(forms.ModelForm):

    # classes taken
    english1Taken = forms.BooleanField(label="English 1", required=False)
    english2Taken = forms.BooleanField(label="English 2", required=False)
    english3Taken = forms.BooleanField(label="English 3", required=False)
    english4Taken = forms.BooleanField(label="English 4", required=False)
    APlitTaken = forms.BooleanField(label="AP Literature", required=False)
    APlangTaken = forms.BooleanField(label="AP Language", required=False)

    preAlgebraTaken = forms.BooleanField(label="Pre-Algebra", required=False)
    algebra1Taken = forms.BooleanField(label="Algebra 1", required=False)
    algebra2Taken = forms.BooleanField(label="Algebra 2", required=False)
    geometryTaken = forms.BooleanField(label="Geometry", required=False)
    preCalculusTaken = forms.BooleanField(label="Pre-Calculus", required=False)
    calculusABTaken = forms.BooleanField(label="Calculus AB", required=False)
    calculusBCTaken = forms.BooleanField(label="Calculus BC", required=False)

    APphysics1Taken = forms.BooleanField(label="AP Physics 1", required=False)
    APphysicsCTaken = forms.BooleanField(label="AP Physics C", required=False)
    chemTaken = forms.BooleanField(label="Chemistry", required=False)
    APchemTaken = forms.BooleanField(label="AP Chemistry", required=False)
    bioTaken = forms.BooleanField(label="Biology", required=False)
    APbioTaken = forms.BooleanField(label="AP Biology", required=False)
    APESTaken = forms.BooleanField(label="AP Environmental Science", required=False)
    APpsychTaken = forms.BooleanField(label="AP Psychology", required=False)

    class Meta:
        model = Profile
        fields = [
            'english1Taken', 'english2Taken', 'english3Taken', 'english4Taken',
            'APlitTaken', 'APlangTaken', 'preAlgebraTaken', 'algebra1Taken', 
            'algebra2Taken', 'geometryTaken', 'preCalculusTaken', 'calculusABTaken', 
            'calculusBCTaken', 'APphysics1Taken', 'APphysicsCTaken', 'chemTaken', 
            'APchemTaken', 'bioTaken', 'APbioTaken', 'APESTaken', 'APpsychTaken'
        ]