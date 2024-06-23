from django.shortcuts import render, redirect  # use for return render, aani redirect
from django.contrib.auth.hashers import make_password  # password hide kara sathi use kelya jate
from store.models.customer import Customer

from django.views import View  # class based view


# class based signup

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        # Customer object create
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)

            # password hash method
            customer.password = make_password(
                customer.password)  # password hide karay sathi -- make_password , aani varti import karaych
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

        # return HttpResponse(request.POST.get('email'))   # ithun "create an account" cha data midto request.POST
        # dictionary madhun value fetch kara sathi-- POST.get('put value name here')

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First name required"
        elif len(customer.first_name) < 4:
            error_message = "first name must br 4 char long or more"

        elif not customer.last_name:
            error_message = ' Last name required'
        elif len(customer.last_name) < 4:
            error_message = ' Last name must br 4 char long or more'

        elif not customer.phone:
            error_message = ' Phone number required'
        elif len(customer.phone) < 10:
            error_message = ' Phone number must be 10 char long'

        elif len(customer.password) < 6:
            error_message = ' Password must be 6 char long'

        elif len(customer.email) < 5:
            error_message = ' Email must be 5 char long'

        elif customer.isExists():
            error_message = 'Email Already Registered..!'

        # saving

        return error_message
