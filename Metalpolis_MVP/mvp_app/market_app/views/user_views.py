from django.shortcuts import render
from common_lib.view_models.buyer.vm_buyer_registration import BuyerViewModel
from common_lib.view_models.User import LogIn
from business_services.logic.buyer_service import BuyerService


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


def validate_user(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print('Validation Started')
    username = "not logged in"
    if request.method == 'POST':
        form = LogIn(request.POST)
        print(form.is_valid())

        # check if form is valid
        email = form.is_valid()
    else:
        form = LogIn()

    return render(request, 'public_site/index.html', {})

