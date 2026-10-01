from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    # keyword search for the dashboard
    list_display = ('id', 'title', 'content')
    search_fields = ('title', 'content')