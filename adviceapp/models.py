from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from timezone_field import TimeZoneField

MENTOR_RATE_CHOICES = (
    (1, '15-20'),
    (2, '20-25'),
    (3, '25-30'),
)

YEAR_CHOICES = (
    (1, 'Less than half a year'),
    (2, 'One year'),
    (3, 'Two to three years'),
    (4, 'Three to five years'),
    (5, 'Five to ten years'),
    (6, 'More than ')
)


class Industry(models.Model):
    """Industry
    """

    industry = models.CharField(max_length=50)

    def __unicode__(self):
        return self.industry


class CareerField(models.Model):
    """CareerField
    """

    career_field = models.CharField(max_length=50)

    def __unicode__(self):
        return self.career_field


class CategoryCorrelation(models.Model):
    """How close the two categories relates to each other
    """

    industry1 = models.ForeignKey(Industry, related_name='+')
    career_field1 = models.ForeignKey(CareerField, related_name='+')

    industry2 = models.ForeignKey(Industry, related_name='+')
    career_field2 = models.ForeignKey(CareerField, related_name='+')

    score = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.id


#class Tag(models.Model):
#    """Customizable tags for searching
#    """

#    name = models.CharField(max_length=50)

#    def __unicode__(self):
#        return self.name


class UserProfile(models.Model):
    """Basic information for each user
    """

    user = models.OneToOneField(User, unique=True)

    #GENDER_CHOICES = (
    #    ('M', 'Male'),
    #    ('F', 'Female')
    #)
    #gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    city = models.CharField(max_length=100, blank=True)

    picture = models.ImageField(upload_to='profilephoto', blank=True)

    linkedin_url = models.URLField(blank=True)

    #time_zone = TimeZoneField(default='America/Los Angeles')

    is_mentor = models.BooleanField()

    def __unicode__(self):
        return str(self.user.username)


def _create_user_profile(sender, instance, created, **kwargs):
    """Create a userProfile for every new user
    """

    if created:
        (profile, created) = UserProfile.objects.get_or_create(user=instance)


# Trigger create_profile when a user is modified
post_save.connect(_create_user_profile, sender=User)


#class BaseProfile(models.Model):
#    """Common information for both mentee and mentor
#    """

    #category = models.ForeignKey(Category)

#    def __unicode__(self):
#        return str(self.user.id)


class MenteeProfile(models.Model):
    """Information for a mentee
    """

    user_profile = models.OneToOneField(UserProfile)
    #user = models.OneToOneField(User, unique=True)

    def __unicode__(self):
        return str(self.user_profile.user.username)


class MentorProfile(models.Model):
    """Information for a mentor
    """

    #user = models.OneToOneField(User, unique=True)

    user_profile = models.OneToOneField(UserProfile)

    rate = models.CharField(max_length=1, choices=MENTOR_RATE_CHOICES)

    bio = models.CharField(max_length=500)

    def __unicode__(self):
        return str(self.user_profile.user.username)


def _class_year(num_of_years):
    """Generate year choices

    num_of_years: number of years to generate
    """

    cur_year = timezone.now().year
    while num_of_years > 0 and cur_year > 0:
        yield (cur_year, cur_year)
        num_of_years -= 1
        cur_year -= 1


class Education(models.Model):
    """Education information
    """

    user_profile = models.ForeignKey(UserProfile)

    school = models.CharField(max_length=100)

    major = models.CharField(max_length=100, blank=True)

    degree = models.CharField(max_length=100, blank=True)

#    year = models.IntegerField(choices=_class_year(50))

#    description = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return str(self.id)


class WorkExperience(models.Model):
    """Working experience
    """

    user_profile = models.ForeignKey(UserProfile)

    title = models.CharField(max_length=100)

    career_field = models.ForeignKey(CareerField)

    company = models.CharField(max_length=100)

    industry = models.ForeignKey(Industry)

    years_of_relevant_experience = models.CharField(max_length=1, choices=YEAR_CHOICES)

    description = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return str(self.id)


#class Skill(models.Model):
#    """Professional skill
#    """
#
#    profile = models.ForeignKey(UserProfile)
#
#    name = models.CharField(max_length=100)
#
#    def __unicode__(self):
#        return str(self.id)


#class Link(models.Model):
#    """Links for related works
#    """

#    profile = models.ForeignKey(UserProfile)

#    url = models.URLField()

#    def __unicode__(self):
#        return str(self.id)


#class CareerGoal(models.Model):
#    """Career goal
#    """

#    company = models.CharField(max_length=100, blank=True)

#    position = models.CharField(max_length=100, blank=True)

#    location = models.CharField(max_length=100, blank=True)

    # Expected age for reaching this goal
#    age = models.PositiveIntegerField(default=0, blank=True)

#    description = models.CharField(max_length=1000, blank=True)

#    category = models.ForeignKey(Category)

#    def __unicode__(self):
#        return str(self.id)


#class Strength(models.Model):
#    """Strength
#    """

#    profile = models.ForeignKey(MenteeProfile)

#    description = models.CharField(max_length=100)

#    def __unicode__(self):
#        return str(self.id)


#class Weakness(models.Model):
#    """Weakness
#    """

#    profile = models.ForeignKey(MenteeProfile)

#    description = models.CharField(max_length=100)

#    def __unicode__(self):
#        return str(self.id)


#class Honor(models.Model):
#    """Honor or awards
#    """

#    profile = models.ForeignKey(MentorProfile)

#    description = models.CharField(max_length=100)

#    def __unicode__(self):
#        return str(self.id)


#class CaseRequest(models.Model):
#    """Request for getting career advice
#    """

#    mentee = models.ForeignKey(User)

#    title = models.CharField(max_length=100)

#    description = models.CharField(max_length=1000)

#    date_created = models.DateTimeField(auto_now_add=True)

#    def __unicode__(self):
#        return str(self.id)


#class MentoringLink(models.Model):
#    """Tracking mentoring relationship and status of invites
#    """

#    case = models.ForeignKey(CaseRequest)

#    mentee = models.ForeignKey(User, related_name='mentoringlinkmentee_set')

#    mentor = models.ForeignKey(User, related_name='mentoringlinkmentor_set')

#    STATUS_CHOICES = (
#        ('R', 'Recommended'),
#        ('I', 'Invited'),
#        ('J', 'Rejected'),
#        ('A', 'Accepted')
#    )
#    status = models.CharField(max_length=1,
#                              choices=STATUS_CHOICES,
#                              default='R')

#    last_status_change = models.DateTimeField()

#    matching_score = models.FloatField(default=0)

#    def __unicode__(self):
#        return str(self.id)


#class AdviceType(models.Model):
#    """Type of advice
#    """

#    name = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.name


#class Advice(models.Model):
#    """Solution/advice for mentee's case
#    """

#    author = models.ForeignKey(User)

#    type = models.ForeignKey(AdviceType)

#    content = models.CharField(max_length=1000)

#    date_created = models.DateTimeField(auto_now_add=True)

#    def __unicode__(self):
#        return str(self.id)


#class Comment(models.Model):
#    """Comment for advice
#    """

#    author = models.ForeignKey(User)

#    advice = models.ForeignKey(Advice, blank=True)

#    comment = models.ForeignKey('self', related_name='+', blank=True, null=True)

#    content = models.CharField(max_length=1000)

#    date_created = models.DateTimeField(auto_now_add=True)

 #   def __unicode__(self):
 #       return str(self.id)


