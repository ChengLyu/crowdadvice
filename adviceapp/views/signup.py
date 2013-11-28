from django import forms
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.utils.translation import ugettext as _

import logging

from adviceapp.manager.category import get_industry_choices, get_field_choices

logger = logging.getLogger(__name__)

class SignupForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    #industry = forms.ChoiceField(choices=get_industry_choices())
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=20,
                                       widget=forms.PasswordInput(),
                                       required=False)
    gender = forms.ChoiceField(choices=[(c,c) for c in ('Male', 'Female', 'N/A')])
    current_location = forms.CharField(max_length=30)
    birthday = forms.DateField()
    career_field = forms.ChoiceField(choices=get_field_choices())


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
                                         password=password,
                                         first_name=cleaned_data.get('first_name'),
                                         last_name=cleaned_data.get('last_name'))
            except(IntegrityError):
                raise forms.ValidationError(_('User already exists'))

        return cleaned_data


#class MentorSignupForm(SignupForm):
