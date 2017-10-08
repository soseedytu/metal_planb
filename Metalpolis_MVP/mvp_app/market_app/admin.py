from django.contrib import admin

# Register your models here.
from common_lib.models import CCodeCategory
from common_lib.models import CCodeTable
from common_lib.models import MCompany
from common_lib.models import MUser
from common_lib.models import MBuyer
from common_lib.models import MSupplier
from common_lib.models import CTags
from common_lib.models import MServices
from common_lib.models import TDocument
from common_lib.models import TRequestForQuotation
from common_lib.models import TSupplierQuotation
from common_lib.models import TDRequiredServices
from common_lib.models import TFileAttachments
from common_lib.models import MDSupplierServices
from common_lib.models import MDServiceParameter
from common_lib.models import TClarifications
from common_lib.models import MDUserRating
from common_lib.models import TDRequiredServicesParameters
from common_lib.models import MDSupplierServiceParameter
from common_lib.models import TTargetedSuppliers

admin.site.register(CCodeCategory)
admin.site.register(CCodeTable)
admin.site.register(MCompany)
admin.site.register(MUser)
admin.site.register(MBuyer)
admin.site.register(MSupplier)
admin.site.register(CTags)
admin.site.register(MServices)
admin.site.register(TDocument)
admin.site.register(TRequestForQuotation)
admin.site.register(TSupplierQuotation)
admin.site.register(TDRequiredServices)
admin.site.register(TFileAttachments)
admin.site.register(MDSupplierServices)
admin.site.register(MDServiceParameter)
admin.site.register(TClarifications)
admin.site.register(MDUserRating)
admin.site.register(TDRequiredServicesParameters)
admin.site.register(MDSupplierServiceParameter)
admin.site.register(TTargetedSuppliers)