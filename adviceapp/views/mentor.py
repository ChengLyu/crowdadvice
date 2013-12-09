__author__ = 'ChengLu'

from django.shortcuts import render, get_object_or_404
from adviceapp.models import UserProfile, MentorProfile, WorkExperience


def dashboard(request):
    return render(request, 'adviceapp/mentor_dashboard.html', {
        'user': request.user,
    })


def directory(request):
    """ List all mentors
    """

    mentor_userprofiles = UserProfile.objects.filter(is_mentor=True)
    return render(request, 'adviceapp/mentor_directory.html', {
        'user': request.user,
        'mentors': mentor_userprofiles,
    })


def profile(request, mentor_id):
    """Mentor Profile
    """

    mentor_userprofile = get_object_or_404(UserProfile, id=mentor_id)
    #mentor_userprofile = UserProfile.objects.get(id=mentor_id)
    work_experiences = WorkExperience.objects.filter(profile=mentor_userprofile)
    return render(request, 'adviceapp/mentor_profile.html', {
        'user': request.user,
        'mentor': mentor_userprofile,
        'work_experiences': work_experiences,
    })

