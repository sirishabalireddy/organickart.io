from django import forms

class login_M(forms.Form):
    username = forms.CharField(required=True, max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

