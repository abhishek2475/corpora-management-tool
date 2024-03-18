# Necessary imports
from django.db import models

class ParallelText(models.Model):
    """
    Model representing parallel texts in different languages (currently three languages).
    """
    en_text = models.TextField()
    hi_text = models.TextField(null=True, blank=True)
    mn_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verify_en_mn = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],null=True, blank=True)
    verify_hi_mn = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],null=True, blank=True)
    verify_en_hi = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],null=True, blank=True)

class DeletionRequest(models.Model):
    """
    Model representing deletion requests for parallel texts.
    """
    parallel_text = models.ForeignKey(ParallelText, on_delete=models.CASCADE)
    requested_by = models.CharField(max_length=255)
    requested_at = models.DateTimeField(auto_now_add=True)
