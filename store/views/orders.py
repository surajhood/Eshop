#
from django.shortcuts import render, redirect  # use for return render, aani redirect
# from django.contrib.auth.hashers import check_password      # password hide kara sathi use kelya jate
from store.models.customer import Customer
from django.views import View  # class based view
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import  auth_middleware            # use of middleware
# from django.utils.decorators import  method_decorator          # method decorator

# class based
class OrderView(View):

    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')   # customer id
        orders = Order.get_orders_by_customer(customer)
        print(orders)

        return render(request, 'orders.html' , {'orders' : orders})


