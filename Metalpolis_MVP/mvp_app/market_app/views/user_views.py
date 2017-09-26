from business_services.logic.buyer_service import BuyerService
from common_lib.view_models.buyer.vm_buyer_registration import BuyerViewModel
from common_lib.view_models.User.LogIn import LoginForm
from django.shortcuts import render
from django.http import HttpResponse

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
    print('Validation Started')
    username = "not logged in"
    if request.method == 'POST':
        print (request.method)
        form = LoginForm(request.POST)
        print(form.is_valid())

        # check if form is valid
        email = form.is_valid()
    else:
        form = LoginForm()

    return render(request, 'buyer/dashboard.html')


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


def buyer_profile(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    print ('Buyer Profile page started')

    return render(request, 'buyer/Profile.html')