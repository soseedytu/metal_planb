from common_lib.models import MCompany


class SupplierService(object):

    def get_supplier_list(self, order_by_col):
        lst_suppliers = MCompany.objects.order_by(order_by_col)  # get last five
        return lst_suppliers

    def register_supplier(self, supplier_obj):
        return None