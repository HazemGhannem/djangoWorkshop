from django import forms
from users.models import Person
from django.contrib.auth.forms import UserCreationForm
 
 
 
class UserRegisterForm(UserCreationForm):   
    class Meta:
        model = Person
        fields = ['username', 'email', 'cin', ]
 
 

class LoginForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['username','passowrd']
    passowrd = forms.CharField(label='password',widget=forms.PasswordInput()
    )