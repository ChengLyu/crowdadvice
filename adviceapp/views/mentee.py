from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import logging
from operator import attrgetter

from adviceapp.models import AdviceType

logger = logging.getLogger(__name__)

@login_required
def plan(request):
    """Render mentee plan page
    """
    
    context = {}
    
    user = request.user
    
    # Redirect to mentor home page, if there is no mentee profile
        
    context['user'] = user
    context['profile'] = request.user.userprofile
    context['advice_types'] = AdviceType.objects.all()
    
    # Get associated mentor links sorted by matching score, highest first
    mentorLinks = sorted(user.mentoringlinkmentee_set.all(),
                         key=attrgetter('matching_score'),
                         reverse=True)
    
    mentors = [ml.getMentorInfo() for ml in mentorLinks]
    
    for m in mentors:
        logger.debug(m['user'].username)

    return render(request, 'adviceapp/mentee_plan.html', context)

