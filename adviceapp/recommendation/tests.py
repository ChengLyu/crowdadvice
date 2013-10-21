__author__ = 'ChengLyu'
# Test file

from adviceapp.models import *
from adviceapp.recommendation.generate_rankings import generate_ranking

# Fetch all the mentees
mentee_list = MenteeProfile.objects.all()

for mentee in mentee_list:
    mentee_id = mentee.user_id
    generate_ranking(mentee_id)
