from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserForm(forms.ModelForm):
    password2= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password','password2']






# from django.contrib.auth.forms import UserCreationForm
# # from .models import User
# from django import forms
# class CustomUserForm(forms.Form):

#     Username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
#     Email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
#     Password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
#     Password_confirmation=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))





# from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class CustomUserForm(UserCreationForm):

#        class Meta:
#           model=User
#           fields=['username','email','password1','password2']































          