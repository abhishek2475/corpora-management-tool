# corpus_manager/views.py

from rest_framework import generics
from .models import ParallelText
from .serializers import ParallelTextSerializer

class ParallelTextListCreate(generics.ListCreateAPIView):
    queryset = ParallelText.objects.all()
    serializer_class = ParallelTextSerializer
