from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views.generic.base import  View, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.debug  import sensitive_post_parameters
from django.utils.decorators import method_decorator

from .forms import RegistrationForm

class EndUserRegistration(FormView):
    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(EndUserRegistration, self).form_valid(form)


class EndUserLogin(FormView):
    """
        form_valid is called when user enters the correct username and password
        form_invalid is called when user enters incorrect username or passord or wrong form submission
        and display the error message according to scenerio.
        default implementation of dispatch is to inspect HTTP method
        and tries to delegate a particular HTTP method

    """
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponse('Logged In')#todo change acc to requirements

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(EndUserLogin, self).dispatch(request, *args, **kwargs)


class Logout(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)



