from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  AuthenticationForm


class RegistrationForm(forms.ModelForm):
    """
     Base class for  users creation. Extend this to get a form that accepts
    user parameters for new user  creation
    """

    username = forms.EmailField(label=_("Email"), max_length=30,
        help_text =_("Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."),
        error_messages ={'invalid': _("Enter a valid email address"), },
        widget=forms.TextInput(attrs={'placeholder': 'Email id'}))
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput(attrs={'placeholder':'Re-enter Pasword'}),
    help_text =_("Enter the same password as above, for verification."))

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    organisation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Organisation'}))


    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'organisation')

    def clean_password1(self):
        password1 = self.cleaned_data["password1"]
        if len(password1) < 5:
            raise forms.ValidationError("Enter a password of min 10 charcters")
        return password1



class LoginAuthenticationForm(AuthenticationForm):

    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField( max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'username','class':'span12'}) )
    password = forms.CharField( widget = forms.PasswordInput(attrs ={'placeholder':'Password','class':'span12'}) )


    def __init__( self, request = None, *args, **kwargs ):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super( AuthenticationForm, self).__init__( *args, **kwargs)


