from django import forms
from django.contrib.auth import (
     authenticate, 
     get_user_model,
     login,
     logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args , **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username =username, password =password)

            if not user:
                raise forms.ValidationError("This user doesnt exist")
        
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
            return super(UserLoginForm , self).clean(*args, **kwargs)


class UserSignUpForm(forms.ModelForm):
   
    password =forms.CharField(widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model= User
        fields = [
            'username',
            'email',            
            'password',               
        ]
    
    def clean_Confirm_Password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('Confirm_Password')        

        if password != password2:
            raise forms.ValidationError("Passwords Mismatch")
        

        return password


        

    

