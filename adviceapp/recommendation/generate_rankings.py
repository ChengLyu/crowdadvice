__author__ = 'ChengLyu'
# Compute the recommendation scores of mentors for ranking

from adviceapp.recommendation.features import *
from adviceapp.recommendation.feature_weights import *
from adviceapp.models import *
from operator import itemgetter
from django.utils import timezone
from adviceapp.models import CategoryCorrelation


def compute_education_score(mentee_educations, mentor_educations):
    return 0


def compute_workexperience_score(mentee_workexperiences, mentor_workexperiences):
    score = 15 # Initial large score number
    for mentee_workexperience in mentee_workexperiences:
        mentee_category = mentee_workexperience[0]
        for mentor_workexperience in mentor_workexperiences:
            mentor_category = mentor_workexperience[0]
            try:
                category_correlation = CategoryCorrelation.objects.get(category1=mentee_category, category2=mentor_category)
            except CategoryCorrelation.DoesNotExist:
                try:
                    category_correlation = CategoryCorrelation.objects.get(category1=mentor_category, category2=mentee_category)
                except CategoryCorrelation.DoesNotExist:
                    continue
            if category_correlation.score < score:
                score = category_correlation.score

    return score


def compute_skill_score(mentee_skills, mentor_skills):
    score = 15 # Initial large score number
    for mentee_skill in mentee_skills:
        mentee_category = mentee_skill[0]
        for mentor_skill in mentor_skills:
            mentor_category = mentor_skill[0]
            try:
                category_correlation = CategoryCorrelation.objects.get(category1=mentee_category, category2=mentor_category)
            except CategoryCorrelation.DoesNotExist:
                try:
                    category_correlation = CategoryCorrelation.objects.get(category1=mentor_category, category2=mentee_category)
                except CategoryCorrelation.DoesNotExist:
                    continue
            if category_correlation.score < score:
                score = category_correlation.score

    return score


def compute_careergoal_score(mentee_careergoals, mentor_workexperiences):
    score = 15
    for mentee_careergoal in mentee_careergoals:
        mentee_category = mentee_careergoal[0]
        for mentor_workexperience in mentor_workexperiences:
            mentor_category = mentor_workexperience[0]
            try:
                category_correlation = CategoryCorrelation.objects.get(category1=mentee_category, category2=mentor_category)
            except CategoryCorrelation.DoesNotExist:
                try:
                    category_correlation = CategoryCorrelation.objects.get(category1=mentor_category, category2=mentee_category)
                except CategoryCorrelation.DoesNotExist:
                    continue
            if category_correlation.score < score:
                score = category_correlation.score

    return score


def compute_advicestats_score(mentee_careergoals, mentor_advicestats):
    score = 15
    for mentee_careergoal in mentee_careergoals:
        mentee_category = mentee_careergoal[0]
        for mentor_advicestat in mentor_advicestats:
            if mentor_advicestat[1] > 0:
                mentor_category = mentor_advicestat[0]
                try:
                    category_correlation = CategoryCorrelation.objects.get(category1=mentee_category, category2=mentor_category)
                except CategoryCorrelation.DoesNotExist:
                    try:
                        category_correlation = CategoryCorrelation.objects.get(category1=mentor_category, category2=mentee_category)
                    except CategoryCorrelation.DoesNotExist:
                        continue
                if category_correlation.score < score:
                    score = category_correlation.score

    return score


def compute_score(mentee_feature, mentor_feature):
    """
        Compute the similarity score between a mentee and a mentor
    """

    # Compute the similarity score between the two education backgrounds
    education_score = compute_education_score(mentee_feature.educations, mentor_feature.educations)
    # Compute the similarity score between the two work_experiences
    workexperience_score = compute_workexperience_score(mentee_feature.work_experiences, mentor_feature.work_experiences)
    # Compute the similarity score between the two skills
    skill_score = compute_skill_score(mentee_feature.skills, mentor_feature.skills)
    # Compute the similarity score between the mentee's career_goals and the mentor's work_experiences
    careergoal_score = compute_careergoal_score(mentee_feature.career_goals, mentor_feature.work_experiences)
    # Compute the similarity score between the mentee's career_goals and the mentor's advice_stats
    advicestats_score = compute_advicestats_score(mentee_feature.career_goals, mentor_feature.advice_stats)

    n = 5

    # Set the feature weights
    w = initialize_weights(n)

    # Compute the final similarity score
    score = education_score*w[0] + workexperience_score*w[1] + skill_score*w[2] + careergoal_score*w[3] + advicestats_score*w[4]
    return score


def generate_ranking(mentee_id):
    """
        Generate the ranking of the mentors intended for a particular mentee
    """

    # Fetch the mentee's information based on the mentee_id
    mentee = MenteeProfile.objects.get(user_id=mentee_id)
    # Construct the feature vector of the mentee
    mentee_feature = MenteeFeature()
    # Education
    educations = mentee.education_set.all()
    for education in educations:
        mentee_feature.educations.append((education.school, education.major))
    # Work Experience
    work_experiences = mentee.workexperience_set.all()
    for work_experience in work_experiences:
        mentee_feature.work_experiences.append((work_experience.category, work_experience.company, work_experience.position, work_experience.end - work_experience.start))
    # Skill
    skills = mentee.skill_set.all()
    for skill in skills:
        mentee_feature.skills.append((skill.category, skill.name))
    # Career Goal
    career_goals = mentee.careergoal_set.all()
    for career_goal in career_goals:
        mentee_feature.career_goals.append((career_goal.category, career_goal.company, career_goal.position))
    # Done with the mentee feature vector creation!

    # Fetch the COMPLETE mentor list
    mentor_list = MentorProfile.objects.all()
    # Initialize the ranking score list
    # ranking_score = []

    # For each mentor:
    #   1. Construct the mentor's feature vector
    #   2. Compute the ranking score between the mentor and the mentee
    for mentor in mentor_list:
        # Construct the mentor's feature vector
        mentor_feature = MentorFeature()
        # Education
        educations = mentor.education_set.all()
        for education in educations:
            mentor_feature.educations.append((education.school, education.major))
        # Work Experience
        work_experiences = mentor.workexperience_set.all()
        for work_experience in work_experiences:
            mentor_feature.work_experiences.append((work_experience.category, work_experience.company, work_experience.position, work_experience.end - work_experience.start))
        # Skill
        skills = mentor.skill_set.all()
        for skill in skills:
            mentor_feature.skills.append((skill.category, skill.name))
        # Advice Stats
        advice_stats = mentor.advicestats_set.all()
        for advice_stat in advice_stats:
            mentor_feature.advice_stats.append((advice_stat.category, advice_stat.count))
        # Done with the mentor feature vector creation!

        # Compute the ranking score between the mentor and the mentee
        score = compute_score(mentee_feature, mentor_feature)
        # Populate the score into database
        # First check if the (mentee, mentor) pair exists
        try:
            mentoringlink_entry = MentoringLink.objects.get(mentee=mentee, mentor=mentor)
        except MentoringLink.DoesNotExist:
            # Construct the (mentee, mentor) pair if not exists.
            mentoringlink_entry = MentoringLink()
            mentoringlink_entry.mentee = mentee.user
            mentoringlink_entry.mentor = mentor.user
            mentoringlink_entry.last_status_change = timezone.now()
        mentoringlink_entry.matching_score = score
        mentoringlink_entry.save()
        # ranking_score.append((mentor.user_id, score))
        del mentor_feature

    # Rank ranking_score
    # ranking_score.sort(key=itemgetter(2))
    # return ranking_score


