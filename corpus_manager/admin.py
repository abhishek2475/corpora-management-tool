from django.contrib import admin
from .models import ParallelText

class ParallelTextAdmin(admin.ModelAdmin):
    list_display = ('source_text', 'target_text', 'verification1', 'verification2', 'verification3', 'verification4', 'verification5')

admin.site.register(ParallelText, ParallelTextAdmin)
