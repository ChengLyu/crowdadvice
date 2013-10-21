from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.http import HttpResponse

from adviceapp.models import MenteeProfile

from adviceapp.recommendation.generate_rankings import generate_ranking

import logging

logger = logging.getLogger(__name__)

# XXX Remove GET after figuring out how to correctly make post against dev server
@require_http_methods(['GET', 'POST'])
def update_all(request):
    """Render mentee plan page
    """
    
    for user in User.objects.all():
        try:
            if user.menteeprofile:
                #logger.debug(user.username)
                # Update score
                generate_ranking(user.id)
        except (MenteeProfile.DoesNotExist):
            logger.debug('User ' + str(user.id) + ' don\'t have menteeprofile')
    
    return HttpResponse()