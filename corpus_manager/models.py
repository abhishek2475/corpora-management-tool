from django.db import models

class ParallelText(models.Model):
    source_text = models.TextField()
    target_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verification1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)],null=True, blank=True)
    verification2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)],null=True, blank=True)
    verification3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)],null=True, blank=True)
    verification4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)],null=True, blank=True)
    verification5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)],null=True, blank=True)
