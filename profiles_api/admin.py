from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from profiles_api.models import UserProfile



# Register your models here.

class CustomUserAdmin(UserAdmin):

    model = UserProfile


admin.site.register(UserProfile)
