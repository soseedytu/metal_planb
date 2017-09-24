from common_lib.models import MCompany


class SupplierService(object):

    def get_supplier_list(self, order_by_col):
        lst_suppliers = MCompany.objects.order_by(order_by_col)  # get last five
        result = {
            'supplier_list': lst_suppliers
        }
        return result

