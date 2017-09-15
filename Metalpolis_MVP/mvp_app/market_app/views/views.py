from django.shortcuts import render
from common_lib.models import MCompany

# Create your views here.
app_label = 'market_app'


def index(request):
    lstSuppliers = MCompany.objects.order_by('Name')  # get last five
    print(lstSuppliers.count())
    dict = {
        'supplier_list': lstSuppliers
    }
    return render(request, 'buyer/index.html', dict)


def detail(request, supplier_id):
    dict = {
        'supplier_list': None
    }
    return render(request, 'buyer/index.html', dict)

