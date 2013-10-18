from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from adviceapp.models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)