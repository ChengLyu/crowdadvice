from django import forms
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.utils.translation import ugettext as _

from adviceapp.models import UserProfile, MentorProfile, MenteeProfile, Education, WorkExperience

import logging

from adviceapp.manager.category import get_industry_choices, get_field_choices

logger = logging.getLogger(__name__)


class SignupForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=20,
                                       widget=forms.PasswordInput(),
                                       required=False)
    gender = forms.ChoiceField(choices=[c for c in (('M','Male'), ('F', 'Female'))])
    current_location = forms.CharField(max_length=30)
    #birthday = forms.DateField()

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
            except IntegrityError:
                raise forms.ValidationError(_('User already exists'))

        return cleaned_data


class MentorSignupForm(SignupForm):
    years_of_relevant_experience = forms.IntegerField()
    career_summary = forms.CharField(max_length=500)


class EducationSignupForm(forms.Form):
    school = forms.CharField(max_length=100)
    major = forms.CharField(max_length=100)
    degree = forms.CharField(max_length=100)


class WorkExperienceSignupForm(forms.Form):
    career_field = forms.ChoiceField(choices=get_field_choices(), required=False)
    year_of_relevant_experience = forms.IntegerField(required=False)
    title = forms.CharField(max_length=100, required=False)
    company = forms.CharField(max_length=100, required=False)
    industry = forms.ChoiceField(choices=get_industry_choices(), required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    description = forms.CharField(max_length=1000, required=False)



