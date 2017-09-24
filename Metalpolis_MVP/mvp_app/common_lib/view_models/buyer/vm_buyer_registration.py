from django import forms


class BuyerViewModel(forms.Form):
    EmailAddress = forms.CharField(max_length=100)
    Password = forms.PasswordInput()
    Username = forms.CharField(max_length=100)
    Title = forms.CharField(max_length=100)
    ContactNumber = forms.CharField(max_length=100)
    MCompany_Id = forms.IntegerField()
