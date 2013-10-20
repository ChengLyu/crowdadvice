from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from adviceapp.models import UserProfile, Education, MenteeProfile, Category,\
                             MenteeProfile, MentorProfile, WorkExperience,\
                             Skill, CareerGoal, AdviceType, AdviceStats,\
                             MentoringLink, Tag

class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]


class EducationInline(admin.StackedInline):
    model = Education


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience


class SkillInline(admin.StackedInline):
    model = Skill


class CareerGoalInline(admin.StackedInline):
    model = CareerGoal


class AdviceStatsInline(admin.StackedInline):
    model = AdviceStats


class MenteeProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, WorkExperienceInline, SkillInline,
               CareerGoalInline]


class MentorProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, WorkExperienceInline, SkillInline,
               AdviceStatsInline]
    
    
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(AdviceType)

admin.site.register(MenteeProfile, MenteeProfileAdmin)
admin.site.register(MentorProfile, MentorProfileAdmin)

admin.site.register(MentoringLink)