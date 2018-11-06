from django.contrib import admin
from django.urls import path, include
from eshopapp.views import IndexPage, ProductView

urlpatterns = [
    
	path('', IndexPage.as_view(), name='indexht'),
	path('product/<slug>/', ProductView.as_view(), name='product_view'),

]