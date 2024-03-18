from rest_framework import serializers
from .models import ParallelText

class ParallelTextSerializer(serializers.ModelSerializer):
    """
    Serializer class for the ParallelText model.

    Serializes the ParallelText model fields into JSON format.
    """

    class Meta:
        model = ParallelText
        fields = ['id', 'english_text', 'hindi_text', 'manipuri_text', 'verify_en_mn', 'verify_hi_mn', 'verify_en_hi', 'created_at']
