from business_services.logic.supplier_service import SupplierService


class BuyerService(object):

    def get_supplier_list(self, order_by_col):
        sup_svs = SupplierService
        lst_suppliers = sup_svs.get_supplier_list(sup_svs, order_by_col)
        return lst_suppliers

    def register_buyer(self, buyer_obj):
        print(buyer_obj)
        #{'EmailAddress': 'abc@abc.com', 'Username': 'abc', 'Title': 'abc', 'ContactNumber': '1231313', 'MCompany_Id': 1}
        print(buyer_obj['Username'])
        print(buyer_obj['EmailAddress'])
        # print(buyer_obj.Password)
        return None

