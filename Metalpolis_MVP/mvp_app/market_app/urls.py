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
    url(r'^validate$', user_views.validate_user, name="validate_user"),

    # http://localhost:8000/market_app/register/supplier
    url(r'^register/supplier$', user_views.register_supplier, name="register_supplier"),

]
