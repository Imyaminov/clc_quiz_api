from django.shortcuts import render
from .models import (Category, Quiz, Question, QuestionOption,
                     ReportQuestion, UserQuiz, UserQuizAnswer)
from .serializers import (CategorySerializers, QuizSerializers, QuestionSerializers,
                          QuestionOptionSerializers, ReportQuestionSerializers, HomePageSerializers)
from rest_framework.views import APIView, Response
from .filters import QuizFilter
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAuthenticated]

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

class CategoryQuizListApiView(generics.ListAPIView):
    serializer_class = HomePageSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.filter(category=self.kwargs['ctg'])
        return queryset

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

class QuestionOptionApiView(generics.ListAPIView):
    serializer_class = QuestionOptionSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        question_id = self.kwargs['id']
        queryset = QuestionOption.objects.filter(questions_id=question_id)
        return queryset

class QuestionApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['title'])
        serializer = QuestionSerializers(question, many=True)
        return Response(serializer.data)

class QuizApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     quiz = Quiz.objects.all()
    #     serializer = QuizSerializers(quiz, many=True)
    #     return Response(serializer.data)

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuizFilter


class HomePageApiView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = HomePageSerializers

    def get_queryset(self):
        return self.queryset.order_by('category')

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("title",)
    ordering_fields = ("category",)

class ReportQuestionApiView(generics.ListAPIView):
    queryset = ReportQuestion.objects.all()
    serializer_class = ReportQuestionSerializers
    permission_classes = [IsAuthenticated]
