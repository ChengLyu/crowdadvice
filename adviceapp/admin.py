from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from adviceapp.models import UserProfile, Education, MenteeProfile, Category,\
                             MenteeProfile, MentorProfile, WorkExperience,\
                             Skill, CareerGoal, AdviceType, AdviceStats,\
                             MentoringLink, Tag, CategoryCorrelation

class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 1


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class CareerGoalInline(admin.StackedInline):
    model = CareerGoal
    extra = 1


class AdviceStatsInline(admin.StackedInline):
    model = AdviceStats
    extra = 1


class MenteeProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, WorkExperienceInline, SkillInline,
               CareerGoalInline]


class MentorProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, WorkExperienceInline, SkillInline,
               AdviceStatsInline]
    
    
class MentoringLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'mentee', 'mentor', 'status', 'matching_score')
    
    
class CategoryCorrelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'category1', 'category2', 'score')
    
    
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category)
admin.site.register(CategoryCorrelation, CategoryCorrelationAdmin)
admin.site.register(Tag)
admin.site.register(AdviceType)

admin.site.register(MenteeProfile, MenteeProfileAdmin)
admin.site.register(MentorProfile, MentorProfileAdmin)

admin.site.register(MentoringLink, MentoringLinkAdmin)