from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

from adviceapp.views.signup import SignupForm
from adviceapp.models import Category, MenteeProfile


def _create_profile(user, form_data):
    """Create mentee profile
    """

    cat = Category.objects.get(main=form_data['industry'], sub=form_data['field'])
    mp = MenteeProfile(user=user, category=cat)

    mp.save()


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])

            _create_profile(user, form.cleaned_data)

            login(request, user)

            return HttpResponseRedirect(reverse('adviceapp:menteeplan'))
    else:
        form = SignupForm()

    return render(request, 'adviceapp/signup.html', {
        'form': form,
        'post_url': 'adviceapp:menteesignup'
    })
