from .models import Quiz
from django_filters import OrderingFilter, FilterSet
from django_filters import rest_framework

class QuizFilter(rest_framework.FilterSet):
    class Meta:
        model = Quiz
        fields = ['grade', 'category']