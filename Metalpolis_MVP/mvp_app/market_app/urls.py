"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from market_app.views import views
from market_app.views import user_views
from public_site.views import views as public_view

# http://localhost:8000/polls
urlpatterns = [
    # http://localhost:8000/polls/
    url(r'^$', views.index, name="index"),
    # http://localhost:8000/market_app/1
    url(r'^(?P<supplier_id>[0-9]+)/$', views.detail, name="detail"),
    # http://localhost:8000/market_app/register
    url(r'^register/$', user_views.registration_main, name="register"),
    # http://localhost:8000/market_app/register/buyer
    url(r'^register/buyer$', user_views.register_buyer, name="register_buyer"),
    # http://localhost:8000/market_app/register/buyer
    # url(r'^login$', user_views.login, name="login"),
    # http://localhost:8000/market_app/buyer/dashboard
    url(r'^buyer/dashboard$', user_views.login, name="auth_login"),
    # http://localhost:8000/market_app/buyer/dashboard
    url(r'^buyer/dashboard$', user_views.buyer_dashboard, name="buyer_dashboard"),
    # http://localhost:8000/market_app/buyer/timeline
    url(r'^buyer/timeline$', user_views.buyer_timeline, name="buyer_timeline"),
    # http://localhost:8000/market_app/buyer/create_rfq
    url(r'^buyer/create_rfq$', user_views.create_rfq, name="buyer_create_rfq"),
    # http://localhost:8000/market_app/buyer/rfq/preview/1
    url(r'^buyer/rfq/preview/(?P<rfq_id>[0-9]+)', user_views.rfq_preview, name="rfq_preview"),
    # http://localhost:8000/market_app/buyer/rfq_list
    url(r'^buyer/rfq_list$', user_views.rfq_list, name="buyer_rfq_list"),
    # http://localhost:8000/market_app/buyer/quotation
    url(r'^buyer/quotation', user_views.quotation, name="buyer_quotation"),
    # http://localhost:8000/market_app/buyer/profile
    url(r'^buyer/profile', user_views.buyer_profile, name="buyer_profile"),
    # http://localhost:8000/market_app/supplier/profile
    url(r'^supplier/profile/(?P<supplier_id>[0-9]+)', user_views.supplier_profile, name="supplier_profile"),
    # http://localhost:8000/market_app/register/supplier
    url(r'^register/supplier$', user_views.register_supplier, name="register_supplier"),
    # http://localhost:8000/public_site/index.html
    url(r'^public_site$', public_view.sign_out, name="sign_out"),
]
