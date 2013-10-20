from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import logging

from adviceapp.models import AdviceType

logger = logging.getLogger(__name__)

@login_required
def plan(request):
    """Render mentee plan page
    """
    
    context = {}
    
    user = request.user
        
    context['user'] = user
    context['profile'] = request.user.userprofile
    context['advice_types'] = AdviceType.objects.all()
    
    logger.debug(user.username)
    
    mentorLinks = user.mentoringlinkmentor_set.all()
    
    for ml in mentorLinks:
        logger.debug(ml.status)
        logger.debug(ml.mentor.username)

    
    return render(request, 'adviceapp/feed.html', context)

