from django.contrib.auth.forms import UserCreationForm
from django import forms
"""
class CustomUserRegistrationForm(UserCreationForm):
    cuny_email = forms.EmailField(required = True)
    major = forms.CharField(required = True)
    CUNY = forms.CharField(required = True)
    graduation_year = forms.IntegerField()
    birth_date = forms.DateField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('cuny.edu'):
            raise forms.ValidationError('Email must be from a valid CUNY')
        return email
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
"""