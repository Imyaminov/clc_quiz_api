from .models import Category, Question, QuestionOption, Quiz, QuizAnswerStats, ReportQuestion

from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'icon', 'slug']


class QuestionOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = "__all__"


class QuestionSerializers(serializers.ModelSerializer):
    questionoption = QuestionOptionSerializers
    class Meta:
        model = Question
        fields = "__all__"


class QuizSerializers(serializers.ModelSerializer):
    # question = QuestionSerializers(many=True)
    class Meta:
        model = Quiz
        fields = ['title', 'created_by', 'img', 'category', 'grade',
                  'times_played', "likes", 'created_at']



class HomePageSerializers(serializers.ModelSerializer):
    # category = CategorySerializers(many=True)
    class Meta:
        model = Quiz
        fields = ['category', 'title', 'img', 'times_played', 'question_count']



class ReportQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportQuestion
        fields = "__all__"