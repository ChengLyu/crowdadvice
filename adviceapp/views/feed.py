from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from adviceapp.models import AdviceType

@login_required
def handle(request):
    """Render feed page
    """
    
    context = {}
    
    user = request.user
        
    context['user'] = user
    context['profile'] = request.user.userprofile
    context['advice_types'] = AdviceType.objects.all()
    
    mentorLinks = user.mentoringlinkmentee_set.all()
    
    for ml in mentorLinks:
        print ml.status
        print ml.mentor.first_name

    
    return render(request, 'adviceapp/feed.html', context)

