from django.shortcuts import render
from common_lib.view_models.User.LogIn import LoginForm
# Create your views here.
app_label = 'public_site'


def index(request):
    print('Validation Started')
    username = "not logged in"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())

        # check if form is valid
        form.is_valid()

    else:
        form = LoginForm()

    return render(request, 'site/index.html')

