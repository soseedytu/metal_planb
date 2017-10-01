from django.shortcuts import render
from business_services.logic.buyer_service import BuyerService

# Create your views here.
app_label = 'market_app'


def index(request):
    svs = BuyerService
    lst_suppliers = svs.get_supplier_list(svs, 'Name')
    result = {
        'supplier_list': lst_suppliers
    }
    return render(request, 'buyer/index.html', result)


def detail(request, supplier_id):
    dict = {
        'supplier_list': None
    }
    return render(request, 'buyer/profile.html', dict)

