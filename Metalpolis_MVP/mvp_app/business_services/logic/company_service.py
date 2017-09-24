from common_lib.models import MCompany


class CompanyService(object):

    def get_company_by_keyword(self, keyword):
        result = MCompany.objects.filter(Name__startswith=keyword)
        return result

