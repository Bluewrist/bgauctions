from django import forms
from.models import Bidds,Contact
from django.contrib.auth.forms import UserCreationForm
from.models import User


class Bidform(forms.ModelForm):
    class Meta:
        model = Bidds
        fields = ('bid_price',)
        widgets = {
            'bid_price':forms.TextInput(attrs={'class':'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

    class Meta:
        model = User
        fields =  ( 'email','password1',)
