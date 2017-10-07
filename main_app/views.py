from django.shortcuts import render, render_to_response
from .models import Product
from .models import Category

def main(request):
	product_place = Product.objects.get(id=1)
	category_place = Category.objects.all()
	return render(request,"index.html", {'product_place': product_place, 'category_place': category_place})