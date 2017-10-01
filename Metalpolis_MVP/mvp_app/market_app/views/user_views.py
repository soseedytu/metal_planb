from business_services.logic.buyer_service import BuyerService
from common_lib.view_models.buyer.vm_buyer_registration import BuyerViewModel
from common_lib.view_models.User.LogIn import LoginForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.forms.utils import ErrorList
from django.contrib import messages
from django import forms
# Create your views here.
app_label = 'market_app_users'


def registration_main(request):
    return render(request, 'registration/main.html')


def register_buyer(request):

    if request.method == 'POST':
        form = BuyerViewModel(request.POST)
        print(form.is_valid())

        # check if form is valid
        if(form.is_valid() == False):
            return render(request, 'registration/register_buyer.html',
                          # {'items': items},
                          {'BuyerVM': form})
        else:
            buyerSvs = BuyerService()
            buyerSvs.register_buyer(form.cleaned_data)
            return render(request, 'registration/register_buyer.html',
                          # {'items': items},
                          {'BuyerVM': form})

    else:
        form = BuyerViewModel()

    return render(request, 'registration/register_buyer.html',
                  #{'items': items},
                  {'BuyerVM': form})


def register_supplier(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    return render(request, 'registration/register_supplier.html')


def login(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    context = {}
    print('Validation Started')
    username = "not logged in"
    _url = 'site/index.html'
    if request.method == 'POST':
        print (request.method)
        form = LoginForm(request.POST)
        print(form.is_valid())
        _url = 'buyer/Dashboard.html'
        # check if form is valid
        if form.is_valid():
            print ('form is valid')
            _email = request.POST['EmailAddress']
            password = request.POST['Password']
            username = User.objects.get(email=_email.lower()).username
            user = authenticate(request,username=username,password=password)
            if user is not None:
                print ('authenticated')
                if user.is_active:
                    print ('user is active')
                    auth_login(request,user)
                    #return render(request, 'buyer/Dashboard.html')
                else:
                    print ('user is not active')
                    context['error'] = 'Non Active User'
                    messages.error(request, 'Non Active User.')
                    _url = 'site/index.html'
            else:
                print ('username or password wrong')
                #return HttpResponse('username or password wrong')
                #raise forms.ValidationError(form.fields['EmailAddress'].error_messages['Bad Username or Password'])
                messages.error(request, 'Bad Username or Password.')
                _url = 'site/index.html'
        else:
            messages.error(request, 'Form is not valid.')
            _url = 'site/index.html'
    else:
        form = LoginForm()
    return render(request, _url)

def buyer_dashboard(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('Buyer Dashboard page started')

    return render(request, 'buyer/Dashboard.html')


def buyer_timeline(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('Buyer Timeline page started')

    return render(request, 'buyer/Timeline.html')


def create_rfq(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('create rfq page started')

    return render(request, 'buyer/CreateRFQ.html')


def rfq_preview(request, rfq_id):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('create rfq page started')

    return render(request, 'buyer/rfq_preview.html')


def rfq_list(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('rfq list page started')

    return render(request, 'buyer/RFQList.html')


def quotation(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('quotation page started')

    return render(request, 'buyer/Quotation.html')


def buyer_profile(request, buyer_id):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('Buyer Profile page started')

    return render(request, 'buyer/profile.html')


def supplier_profile(request, supplier_id):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('Supplier Profile page started')

    return render(request, 'supplier/profile.html')

