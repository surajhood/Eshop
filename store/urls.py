from django.contrib import admin  # include this same from Eshop\urls.py
from django.urls import path, include  # # include this same from Eshop\urls.py

# from .views import home, login, signup  # function based use small :- login , signup, index

# urlpatterns = [
#     path('', home.index, name='homepage'),
#     # path('signup', signup),
#     path('signup', signup.Signup.as_view(), name='signup'),
#     # path('login', login)  # function based
#     path('login', login.Login.as_view(), name='login')
# ]



from .views.home import Index
from .views.signup import  Signup
from .views.login import  Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware        # middleware- method decorator

urlpatterns = [
    # path('', index, name='homepage'),                                # function based
    path('', Index.as_view(), name='homepage'),
    # path('signup', signup),                                          # function based
    path('signup', Signup.as_view(), name='signup'),
    # path('login', login),                                            # function based
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),                             # function based
    path('cart', Cart.as_view(), name='cart'),                         # class based
    path('check-out', CheckOut.as_view(), name='checkout'),            # class based
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),                    # class based

]