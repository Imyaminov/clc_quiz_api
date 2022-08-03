from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryListApiView.as_view(), name='category'),  # list of categories
    path('quiz/', QuizApiView.as_view(), name='quiz'),  # list of quizzes
    path('home/', HomePageApiView.as_view(), name='home'),  # search quiz by title
    path('question/<str:title>', QuestionApiView.as_view(), name='question'),  # quiz - question - questionOption
    path('option/<int:id>', QuestionOptionApiView.as_view(), name='question_option'),  # question - questionOption
    path('home/<str:ctg>', CategoryQuizListApiView.as_view(), name='category_quiz'),  # list quizzes in specific searched category


    path('report/', ReportQuestionApiView.as_view(), name='report'),  # report issue for quiz, question

]
