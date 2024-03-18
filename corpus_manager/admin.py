# Necessary imports
from django.contrib import admin
from .models import ParallelText

class ParallelTextAdmin(admin.ModelAdmin):
    """
    Admin class for managing ParallelText model in the Django admin interface.
    """
    list_display = ('en_text', 'hi_text', 'mn_text', 'verify_en_mn', 'verify_hi_mn', 'verify_en_hi')

# Register the ParallelText model with the ParallelTextAdmin class in the Django admin interface
admin.site.register(ParallelText, ParallelTextAdmin)
