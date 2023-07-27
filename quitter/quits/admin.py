from django.contrib import admin
from .models import Quit


@admin.register(Quit)
class QuitAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'display_tagged_people', 'user']
    list_filter = ['photo', 'user']
    ordering = ['title', 'user']

    def display_tagged_people(self, obj):
        return ", ".join([person.username for person in obj.tagged_people.all()])

    display_tagged_people.short_description = "Tagged People"
