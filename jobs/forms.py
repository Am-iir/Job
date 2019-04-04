from django import forms

from .models import SignUp
from .models import Job

class SignUpForm(forms.ModelForm):
    class Meta:
        model= SignUp
        fields = [ 'email', 'full_name']

class JobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields = [ 'title', 'company_name' ,'description']

