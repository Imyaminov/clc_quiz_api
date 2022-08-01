from django.shortcuts import render
from .models import (Category, Quiz, Question, QuestionOption,
                     ReportQuestion, StartQuiz, QuizAnswerStats)
from .serializers import (CategorySerializers, QuizSerializers, QuestionSerializers,
                          QuestionOptionSerializers, ReportQuestionSerializers, HomePageSerializers)
from .filters import QuizFilter
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]

class QuestionOptionApiView(generics.ListAPIView):
    serializer_class = QuestionOptionSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        question_id = self.kwargs['id']
        queryset = QuestionOption.objects.filter(questions_id=question_id)
        return queryset

class QuestionApiView(generics.ListAPIView):
    serializer_class = QuestionSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        quiz_id = self.kwargs['id']
        queryset = Question.objects.filter(quiz__id=quiz_id)
        return queryset

class QuizApiView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title",)
    ordering_fields = ("times_played", "likes")

    filterset_class = QuizFilter

class HomePageApiView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = HomePageSerializers
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs['id'])

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title",)
    ordering_fields = ("times_played", "likes")


class ReportQuestionApiView(generics.ListAPIView):
    queryset = ReportQuestion.objects.all()
    serializer_class = ReportQuestionSerializers
    permission_classes = [IsAuthenticated]
