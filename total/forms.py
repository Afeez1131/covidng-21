from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = '', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<small><ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul></small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Verify Password'
        self.fields['password2'].help_text = ''
        self.fields['password2'].help_text = '<small><ul><li>Enter the same password as before, for verification.</li></ul></small>'

# class ContactForm(forms.Form):
#     username = forms.CharField(label='',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    message = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
