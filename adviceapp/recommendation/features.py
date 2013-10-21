__author__ = 'ChengLyu'
# Definitions of Mentors and Mentees' feature vectors

import adviceapp.models


# Base feature vector
class BaseFeature:
    # Education
    educations = [] # Unit Tuple (school, major)
    # Work experience
    work_experiences = [] # Unit Tuple (category, company, position, duration)
    # Skill
    skills = [] # Unit Tuple (category, name/identifier)


# Mentee's feature vector
class MenteeFeature(BaseFeature):
    # Career Goal
    career_goals = [] # Unit Tuple (category, company, position)


# Mentor's feature vector
class MentorFeature(BaseFeature):
    # Advice Stats
    advice_stats = [] # Unit Tuple (category, count)