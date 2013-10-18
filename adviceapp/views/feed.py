from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def handle(request):
    """Render feed page
    """
    
    user = request.user
    profile = user.userprofile
    
    return render(request,
                  'adviceapp/feed.html',
                  {
                      'user' : user,
                      'profile' : profile
                  })

