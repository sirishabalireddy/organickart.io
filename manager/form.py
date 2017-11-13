from django import forms

class login_M(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

