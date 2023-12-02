# for registering new user
from django.contrib.auth.models import User

# for creating or updating records
from .models import Record

# for registering users or records
from django import forms

# for registering new user and login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 

# for registering new user and login
from django.forms.widgets import PasswordInput, TextInput


# Create a user

class CreateUserForm(UserCreationForm):
    
    username = forms.CharField(label='Uživatelské jméno', widget=forms.TextInput)
    password1 = forms.CharField(label='Nové heslo', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Zadejte heslo znovu pro kontrolu', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Uživatelské jméno', widget=TextInput())
    password = forms.CharField(label='Heslo', widget=PasswordInput())
    

# Create a record

class CreateRecordForm(forms.ModelForm):

    first_name = forms.CharField(label='Jméno', widget=forms.TextInput)
    last_name = forms.CharField(label='Příjmení', widget=forms.TextInput)
    email = forms.CharField(label='Email', widget=forms.TextInput)
    phone = forms.CharField(label='Telefon', widget=forms.TextInput)
    address = forms.CharField(label='Ulice a č. p.', widget=forms.TextInput)
    city = forms.CharField(label='Město', widget=forms.TextInput)
    country = forms.CharField(label='Stát', widget=forms.TextInput)


    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country' ]


# Update a record

class UpdateRecordForm(forms.ModelForm):

    first_name = forms.CharField(label='Jméno', widget=forms.TextInput)
    last_name = forms.CharField(label='Příjmení', widget=forms.TextInput)
    email = forms.CharField(label='Email', widget=forms.TextInput)
    phone = forms.CharField(label='Telefon', widget=forms.TextInput)
    address = forms.CharField(label='Ulice a č. p.', widget=forms.TextInput)
    city = forms.CharField(label='Město', widget=forms.TextInput)
    country = forms.CharField(label='Stát', widget=forms.TextInput)

    class Meta:

        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country' ]
