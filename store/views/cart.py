#
from django.shortcuts import render, redirect               # use for return render, aani redirect
# from django.contrib.auth.hashers import check_password      # password hide kara sathi use kelya jate
# from store.models.customer import Customer
from django.views import View                               # class based view
from store.models.product import Product

# class based
class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})


