from django.contrib import admin
from django.urls import path, include
from eshopapp.views import IndexPage

urlpatterns = [
    
	path('', IndexPage.as_view(), name='indexht'),

]