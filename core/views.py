from django.contrib.auth.forms import AuthenticationForm
from django.template.context import RequestContext
from django.views.generic.base import  View, TemplateView
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from .forms import RegistrationForm


#todo use form view insead of template view/
class EndUserRegistration(TemplateView):
    template_name = ''

    def post(self, request, *args, **kwargs):
        registration_form = RegistrationForm(data=self.request.POST)
        if registration_form.is_valid():
            registration_form.save()
            form = AuthenticationForm(data=request.POST)
            auth_login(request, authenticate(username=request.POST['email'], password=request.POST['password1']))
            #todo return to sucess page
        #todo return to same page with errors