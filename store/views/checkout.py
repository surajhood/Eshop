
from django.shortcuts import render, redirect  # use for return render, aani redirect
from django.contrib.auth.hashers import check_password      # password hide kara sathi use kelya jate
from store.models.customer import Customer
from django.views import View  # class based view
from store.models.product import Product
from store.models.orders import Order


# class based
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order1 = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order1.save()
        request.session['cart'] = {}  # session cart clear krne

        return redirect('cart')
