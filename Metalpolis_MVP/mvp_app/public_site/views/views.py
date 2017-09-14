from django.shortcuts import render

# Create your views here.
app_label = 'public_site'


def index(request):
    return render(request, 'site/index.html')

