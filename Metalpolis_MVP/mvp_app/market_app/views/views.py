from django.shortcuts import render
from business_services.services.buyer_service import SupplierService

# Create your views here.
app_label = 'market_app'


def index(request):
    svs = SupplierService
    result = svs.get_supplier_list(svs, 'Name')
    return render(request, 'buyer/index.html', result)


def detail(request, supplier_id):
    dict = {
        'supplier_list': None
    }
    return render(request, 'buyer/index.html', dict)

