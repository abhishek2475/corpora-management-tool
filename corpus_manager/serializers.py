from rest_framework import serializers
from .models import ParallelText

class ParallelTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParallelText
        fields = ['id', 'source_text', 'target_text', 'created_at','verification1', 'verification2', 'verification3', 'verification4', 'verification5']
