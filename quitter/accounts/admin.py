from datetime import date
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import QuitterUser

# Register your models here.

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'date_of_birth', 'gender']
    list_filter = ['username', 'email']
    ordering = ['username', 'email']

    def clean_date_of_birth(self):
        date_of_birth = self.date_of_birth
        if date_of_birth and date_of_birth > date.today():
            raise ValidationError("You cannot add upcoming date!")
        return date_of_birth

    def add_to_my_group(self, request, queryset):
        group = Group.objects.get(name="Super Admins")
        for user in queryset:
            user.groups.add(group)
    add_to_my_group.short_description = "Add To Super Admins"
    actions = [add_to_my_group]
