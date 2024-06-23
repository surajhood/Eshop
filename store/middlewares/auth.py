from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.session.get('customer'))
        returnUrl = request.META['PATH_INFO']           # login kelya vr tyach page vr return jay sathi , jithun aalo hoto
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):    # jr customer nahi midala
            return redirect(f'login?return_url={returnUrl}')



        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.


        return response

    return middleware