from common_lib.models import CCodeTable, CCodeCategory


class BuyerService(object):

    def get_codes_by_category(self, category_id):
        result = CCodeTable.objects.filter(CCodeCategory_Id=category_id)
        return result