from django import forms
from common_lib.models import MUser


class LoginForm(forms.Form):
    EmailAddress = forms.CharField(max_length=100)
    Password = forms.PasswordInput()

    def clean(self):
        email = self.cleaned_data.get("EmailAddress")
        Upass = self.cleaned_data.get("Password")
        user = MUser.objects.filter(EmailAddress=email).filter(Password=Upass)
        if not user:
            raise forms.ValidationError("User does not exist!")
        return email
