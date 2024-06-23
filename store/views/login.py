
from django.shortcuts import render, redirect , HttpResponseRedirect    # use for return render, aani redirect
from django.contrib.auth.hashers import check_password      # password hide kara sathi use kelya jate
from store.models.customer import Customer
from django.views import View                               # class based view


# class based
class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')  # 'POST' in dictionary form
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:  # jr customer cha email midala
            flag = check_password(password, customer.password)  # password encoding
            if flag:                                            # value True aali tr
                request.session['customer'] = customer.id         # session decleard

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Email or password invalid..!"
        else:  # jr customer cha email nahi
            error_message = "Email or password invalid..!"
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()

    return redirect('login')

