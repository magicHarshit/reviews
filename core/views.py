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

from .forms import RegistrationForm

class EndUserRegistration(FormView):
    User = get_user_model()
    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super(EndUserRegistration, self).get_context_data(**kwargs)
        data['registration_form'] = data.get('form')
        return data

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(EndUserRegistration, self).form_valid(form)


    