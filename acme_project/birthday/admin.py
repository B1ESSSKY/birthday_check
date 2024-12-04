from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name', 'birthday')
    list_display_links = ('first_name', 'last_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag',)
