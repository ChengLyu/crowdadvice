from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import logging
from operator import attrgetter

#from adviceapp.models import AdviceType

logger = logging.getLogger(__name__)

@login_required
def create_profile(request):
    """Create mentee profile
    """
    
    return render(request, 'adviceapp/mentee_create_profile.html')

@login_required
def plan(request):
    """Render mentee plan page
    """
    
    context = {}
    
    user = request.user
    
    # Redirect to mentor home page, if there is no mentee profile
        
    context['user'] = user
    context['profile'] = request.user.userprofile
    
    advice_types = AdviceType.objects.all()
    
    # Get associated mentor links sorted by matching score, highest first
    mentor_links = sorted(user.mentoringlinkmentee_set.all(),
                         key=attrgetter('matching_score'),
                         reverse=True)
    
    mentors = [{'user': ml.mentor, 'status': ml.status} for ml in mentor_links]
    context['mentors'] = mentors
    
    advice_type_to_mentor = []
    
    for a in advice_types:
        filtered_links = filter(lambda item: a in set(item.advice_types.all()),
                                mentor_links)
        advice_type_to_mentor.append({
            'advice_type': a,
            'mentors': [ml.mentor for ml in filtered_links]})
        
    context['advice_types'] = advice_type_to_mentor

    return render(request, 'adviceapp/mentee_plan.html', context)

