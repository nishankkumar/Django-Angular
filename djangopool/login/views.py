from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import authenticate

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 

 # class LoginForm():
    # username = 

def login_page(request):
    from django.template import RequestContext
    context = {}
    return render_to_response(
        'registration/login.html',
        context,
        context_instance=RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

class Login_page( View):
    email = ''
    password = ''
    def post(self, request, *args, **kwargs):
        self.email = request.POST['email']
        self.password = request.POST['password']
        print "look at self.email"
        print self.email
        print self.password
        user = authenticate(email=self.email, password=self.password)
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return render_to_response(
                'registration/success.html',
                )
            else:
                # Return a 'disabled account' error message
                return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/error')

 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
    


# class IndexPageView(TemplateView):
#     template_name = '/home.html'

    # def get(self, request, *args, **kwargs):
    #     if request.flavour == commons_constants.MOBILE_FLAVOUR:
    #         if (request.user.is_owner or request.user.is_admin) and not request.user.company.all_steps_completed:
    #             return render_to_response('mobile/companies/company_profile/post_sign_onboarding_process.html')
    #         return super(IndexPageView, self).get(request, *args, **kwargs)
    #     else:
    #         return HttpResponseRedirect(reverse('jobs:techs_calendar'))

