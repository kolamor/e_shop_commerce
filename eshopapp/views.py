from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from eshopapp.models import Category, Brand, Product
from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def product_paginator(paginator, page_number):
	
	page = paginator.get_page(page_number)

	is_paginator = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	return (page, prev_url, next_url)



class IndexPage(View):
	""" Index Html"""
	def get(self, request):
		search_query = request.GET.get('search', '')

		if search_query:
			products_list = Product.objects.filter(Q(title__icontains=search_query) |
											Q(text__icontains=search_query))
		else:
			products_list = Product.objects.filter(available=True)
		
		paginator = Paginator(products_list,2)
		page_number = request.GET.get('page', 1)
		page, prev_url, next_url = product_paginator(paginator, page_number)
		formlogin = LoginForm()
		
		category = get_object_or_404(Category)

		

		context ={
				
				'category' : category,
				'page_object': page,
		        'next_url'   : next_url,
		        'prev_url'   : prev_url,
		        'formlogin'  : formlogin,
		        
		}

		return render(request,'index.html', context)


class ProductView(View):
	"""Full product discription"""
	def get(self, request, slug):
		product_full = get_object_or_404(Product, slug=slug)
		context = {
				'product' : product_full
		}
		return render(request, 'product_full.html', context)