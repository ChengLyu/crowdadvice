from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

from django.forms.models import modelformset_factory
from adviceapp.views.signup import MentorSignupForm, EducationSignupForm, WorkExperienceSignupForm
from adviceapp.models import UserProfile, MentorProfile, WorkExperience


def _create_profile(user, form):
    """Create mentor profile
    """

    #cat = Category.objects.get(industry=form['industry'], career_field=form['field'])
    #up = UserProfile(user=user, gender=form['gender'], current_location=form['current_location'])
    #up.save()
    user_profile = UserProfile.objects.get(user=user)
    user_profile.gender = form['gender']
    user_profile.current_location = form['current_location']
    user_profile.linkedin_url = form['linkedin_url']
    user_profile.is_mentor = True
    user_profile.save()
    mentor_profile = MentorProfile(user_profile=user_profile, years_of_relevant_experience=form['years_of_relevant_experience'], career_summary=form['career_summary'])
    mentor_profile.save()


def signup(request):
    #EducationFormSet = formset_factory(EducationSignupForm, extra=5)
    #WorkExperienceFormSet = formset_factory(WorkExperienceSignupForm,extra=2)

    if request.method == 'POST':
        form = MentorSignupForm(request.POST)
        #education_formset = EducationFormSet(request.POST, request.FILES, prefix='education')
        #workexperience_formset = WorkExperienceFormSet(request.POST, request.FILES, prefix='workexperience')

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])

            _create_profile(user, form.cleaned_data)

            login(request, user)

            return HttpResponseRedirect(reverse('adviceapp:mentorworksignup'))
    else:
        form = MentorSignupForm()
        #education_formset = EducationFormSet(prefix='education')
        #workexperience_formset = WorkExperienceFormSet(prefix='workexperience')

    return render(request, 'adviceapp/signup.html', {
        'page_mark': True,
        'form': form,
       # 'education_formset': education_formset,
        #'workexperience_formset': workexperience_formset,
        'post_url': 'adviceapp:mentorsignup',
    })


def signup_work(request):
    # First check whether there has been at least one work experience filled in
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.is_mentor:
        try:
            work_experience = WorkExperience.objects.get(profile=user_profile)
            return HttpResponseRedirect(reverse('adviceapp:mentordashboard'))
        except WorkExperience.DoesNotExist:
                WorkExperienceFormSet = modelformset_factory(WorkExperience, exclude='profile')
                if request.method == 'POST':
                    workexperience_formset = WorkExperienceFormSet(request.POST, request.FILES)
                    if workexperience_formset.is_valid():
                        #user_profile = UserProfile.objects.get(user=request.user)
                        for form in workexperience_formset.forms:
                            work_experience = form.save(commit=False)
                            work_experience.profile_id = user_profile.id
                            work_experience.save()
                        return HttpResponseRedirect(reverse('adviceapp:mentordashboard'))
                else:
                    workexperience_formset = WorkExperienceFormSet(queryset=WorkExperience.objects.none())

                return render(request, 'adviceapp/signup.html', {
                    'page_mark': False,
                    'formset': workexperience_formset,
                    'post_url': 'adviceapp:mentorworksignup',
                })
    else:
        return HttpResponseRedirect(reverse('adviceapp:menteecreateprofile'))