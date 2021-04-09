from django import forms

class SignUp(forms.Form):
    usern = forms.CharField(max_length=200, required=False)
    email = forms.CharField(max_length=200, required=False) # em stands for email
    passw = forms.CharField(max_length=200, required=False)


class Login(forms.Form):
    usern = forms.CharField(max_length=200, required=False)
    passw = forms.CharField(max_length=200, required=False)
