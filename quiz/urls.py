from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryApiView.as_view(), name='category'),
    path('question/<int:id>', QuestionApiView.as_view(), name='question'),
    path('option/<int:id>', QuestionOptionApiView.as_view(), name='question_option'),
    path('quiz/', QuizApiView.as_view(), name='quiz'),
    path('home/<int:id>', HomePageApiView.as_view(), name='home'),


    path('report/', ReportQuestionApiView.as_view(), name='report'),

]
