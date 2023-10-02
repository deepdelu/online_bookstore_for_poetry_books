from django import forms
from app1.models import registration
from app1.models import cont 
from app1.models import base
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registrationform(forms.ModelForm):
    name=forms.CharField(max_length=100)
    phone=forms.CharField(max_length=10)
    pincode=forms.CharField(max_length=6)
    email=forms.CharField(max_length=20)
    address=forms.CharField(max_length=100)
    class Meta:
        model=registration
        fields='__all__'

class contform(forms.ModelForm):
    name=forms.CharField(max_length=100)
    email=forms.CharField(max_length=20)
    phone=forms.CharField(max_length=10)
    message=forms.CharField(max_length=100)
    class Meta:
        model=cont
        fields='__all__'
        
class baseform(forms.ModelForm):
    email=forms.CharField(max_length=20)
    class Meta:
        model=base
        fields='__all__'

class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'username',
            'password1',
            'password2'
        ]
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user