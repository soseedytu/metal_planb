from django import forms
from common_lib.models import MUser
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    EmailAddress = forms.CharField(max_length=100)
    Password = forms.PasswordInput()

    def clean(self):

        email = self.cleaned_data.get("EmailAddress")
        upass = self.cleaned_data.get("Password")
        print("password")
        print(upass)
        auth_user = MUser.objects.filter(EmailAddress=email)
        #user = MUser.objects.get(EmailAddress=email)
        print(auth_user)
        if not auth_user:
            print("error!")
            raise forms.ValidationError("User does not exist!")
        else:
            return auth_user
