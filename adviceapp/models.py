from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


class Category(models.Model):
    """Career fields
    """
    
    main = models.CharField(max_length=50)
    
    sub = models.CharField(max_length=50)


class Tag(models.Model):
    """Customizable tags for searching
    """
    
    name = models.CharField(max_length=50)


class UserProfile(models.Model):
    """Basic information for each user
    """
    
    user = models.OneToOneField(User, unique=True)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    
    current_location = models.CharField(max_length=100)
    
    birthday = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return str(self.user.id)


def _create_user_profile(sender, instance, created, **kwargs):
    """Create a userProfile for every new user
    """
    
    if created:
        (profile, created) = UserProfile.objects.get_or_create(user=instance)

# Trigger create_profile when a user is modified
post_save.connect(_create_user_profile, sender=User)


class BaseProfile(models.Model):
    """Common information for both mentee and mentor
    """
    
    user = models.OneToOneField(User, unique=True)
    
    class Meta:
        abstract = True


class MenteeProfile(BaseProfile):
    """Information for a mentee
    """
    pass


class MentorProfile(BaseProfile):
    """Information for a mentee
    """
    pass


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
    
    profile = models.ForeignKey(BaseProfile)
    
    school = models.CharField(max_length=100)
    
    major = models.CharField(max_length=100)
    
    year = models.IntegerField(choices=_class_year(50))


class WorkExperience(models.Model):
    """Working experience
    """
    
    profile = models.ForeignKey(BaseProfile)
    
    company = models.CharField(max_length=100)
    
    position = models.CharField(max_length=100)
    
    location = models.CharField(max_length=100)
    
    description = models.CharField(max_length=1000)
    
    start = models.DateField()
    
    end = models.DateField()
    
    category = models.ForeignKey(Category)
    
    tags = models.ManyToManyField(Tag)


class Skill(models.Model):
    """Professional skill
    """
    
    profile = models.ForeignKey(BaseProfile)
    
    name = models.CharField(max_length=100)
    
    category = models.ForeignKey(Category)
    
    tags = models.ManyToManyField(Tag)
    
    
class CareerGoal(models.Model):
    """Career goal
    """
    
    profile = models.ForeignKey(MenteeProfile)
    
    company = models.CharField(max_length=100)
    
    position = models.CharField(max_length=100)
    
    location = models.CharField(max_length=100)
    
    # Expected age for reaching this goal
    age = models.PositiveIntegerField()
    
    description = models.CharField(max_length=1000)
    
    category = models.ForeignKey(Category)
    
    tags = models.ManyToManyField(Tag)
    

class AdviceType(models.Model):
    """Type of advice
    """
    
    name = models.CharField(max_length=100) 

    
class AdviceStats(models.Model):
    """Stats regarding a mentor's contribution
    """
    
    profile = models.ForeignKey(MentorProfile)
    
    type = models.ForeignKey(AdviceType)
    
    category = models.ForeignKey(Category)
    
    count = models.PositiveIntegerField()
    
