from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext as _

import logging

logger = logging.getLogger(__name__)

class SignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=20,
                                       widget=forms.PasswordInput(),
                                       required=False)

    def clean(self):
        """Check if passwords match
        """

        cleaned_data = super(SignupForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and password != confirm_password:
            self._errors["password"] =\
                self.error_class([_('Passwords don\'t match')])

            del cleaned_data["password"]
            del cleaned_data["confirm_password"]
        elif not self._errors:
            try:
                User.objects.create_user(email,
                                         email=email,
                                         password=password)
            except(IntegrityError):
                raise forms.ValidationError(_('User already exists'))

        return cleaned_data


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            login(request, user)

            return HttpResponseRedirect(reverse('adviceapp:menteeplan'))
    else:
        form = SignupForm()

    return render(request, 'adviceapp/signup.html', {
        'form': form,
    })