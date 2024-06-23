# from django.shortcuts import render, redirect  # use for return render, aani redirect
# from django.http import HttpResponse            # use for return HttpResponse
# from django.contrib.auth.hashers import make_password, check_password   # password hide kara sathi use kelya jate
# from .models.product import Product
# from .models.product import Category
# from .models.customer import Customer
# from django.views import View            # class based view


from django.shortcuts import render , redirect
from store.models.product import Product
from store.models.product import Category
from django.views import View



# to check hash password in 'terminal
# print(make_password('1234'))
# print(check_password('1234', 'pbkdf2_sha256$390000$HevbeOZTeCxVwxEfSAU2Fa$OydNeh2eyGGM7fZIsNXhd83tq2apF9p0YybwJlOU0xw=',))

# Create your views here.


# class based Index
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')     # session se cart access krna
        if cart:                               # jar cart hot session madhe
            quantity = cart.get(product)       # quantity jar midala
            if quantity:                       # quantity jar midala
                if remove:                     # remove nam ki value mere pass hai to quantity minus karna hai
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:                              # quantity jar nahi midali
                cart[product] = 1
        else:                                  # jar cart session madhe nahi hot
            cart = {}                          # new cart add krne
            cart[product] = 1                  # he changes session madhe add karayche ahe

        request.session['cart'] = cart          # cart session madhe add kel
        print('cart' ,request.session['cart'])
        return redirect('homepage')


    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        print('you are: ', request.session.get('email'))
        return render(request, 'index.html', data)








# function based index
# def index(request):
#     products = None
#     categories = Category.get_all_categories()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         products = Product.get_all_products();
#     data = {}
#     data['products'] = products
#     data['categories'] = categories
#     print('you are: ' , request.session.get('email'))
#     return render(request, 'index.html', data)


# def validateCustomer(customer):
#     error_message = None;
#     if (not customer.first_name):
#         error_message = "First name required"
#     elif len(customer.first_name) < 4:
#         error_message = "first name must br 4 char long or more"
#
#     elif not customer.last_name:
#         error_message = ' Last name required'
#     elif len(customer.last_name) < 4:
#         error_message = ' Last name must br 4 char long or more'
#
#     elif not customer.phone:
#         error_message = ' Phone number required'
#     elif len(customer.phone) < 10:
#         error_message = ' Phone number must be 10 char long'
#
#     elif len(customer.password) < 6:
#         error_message = ' Password must be 6 char long'
#
#     elif len(customer.email) < 5:
#         error_message = ' Email must be 5 char long'
#
#     elif customer.isExists():
#         error_message = 'Email Already Registered..!'
#
#     # saving
#
#     return error_message

# def registerUser(request):
    # postData = request.POST
    # first_name = postData.get('firstname')
    # last_name = postData.get('lastname')
    # phone = postData.get('phone')
    # email = postData.get('email')
    # password = postData.get('password')
    #
    # # validation
    # value = {
    #     'first_name': first_name,
    #     'last_name': last_name,
    #     'phone': phone,
    #     'email': email
    # }
    # error_message = None
    # # Customer object create
    # customer = Customer(first_name=first_name,
    #                     last_name=last_name,
    #                     phone=phone,
    #                     email=email,
    #                     password=password)
    # error_message = validateCustomer(customer)
    #
    # if not error_message:
    #     print(first_name, last_name, phone, email, password)
    #
    #     # password hash method
    #     customer.password = make_password(
    #         customer.password)  # password hide karay sathi -- make_password , aani varti import karaych
    #     customer.register()
    #     return redirect('homepage')
    # else:
    #     data = {
    #         'error': error_message,
    #         'values': value
    #     }
    #     return render(request, 'signup.html', data)
    #
    # # return HttpResponse(request.POST.get('email'))   # ithun "create an account" cha data midto request.POST
    # # dictionary madhun value fetch kara sathi-- POST.get('put value name here')

# function based signup
# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)         # 'POST' method aali tr





# function based login
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')   # 'POST' in dictionary form
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:                                     # jr customer cha email midala
#             flag = check_password(password , customer.password)  # password encoding
#             if flag:                                        # value True aali tr
#                 return redirect('homepage')
#             else :
#                 error_message = "Email or password invalid..!"
#         else:                                            # jr customer cha email nahi
#             error_message = "Email or password invalid..!"
#         print(email , password)
#         return render(request, 'login.html',{'error' : error_message})