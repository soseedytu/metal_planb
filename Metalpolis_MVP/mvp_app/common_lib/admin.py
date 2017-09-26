from django.contrib import admin
from .models import CCodeCategory
from .models import CCodeTable
from .models import MCompany
from .models import MUser
from .models import MBuyer
from .models import MSupplier
from .models import CTags
from .models import MServices
from .models import TDocument
from .models import TRequestForQuotation
from .models import TSupplierQuotation
from .models import TDRequiredServices
from .models import TFileAttachments
from .models import MDSupplierServices
from .models import MDServiceParameter
from .models import TClarifications
from .models import MDUserRating
from .models import TDRequiredServicesParameters
from .models import MDSupplierServiceParameter
from .models import TTargetedSuppliers

# Register your models here.
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