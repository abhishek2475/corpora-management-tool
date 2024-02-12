# corpus_manager/models.py

from django.db import models

class ParallelText(models.Model):
    source_text = models.TextField()
    target_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
