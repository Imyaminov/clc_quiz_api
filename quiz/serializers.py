from .models import Category, Question, QuestionOption, Quiz, ReportQuestion

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
    # quiz = serializers.StringRelatedField()
    options = QuestionOptionSerializers(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['title', 'type', 'points', 'time', 'options']


class QuizSerializers(serializers.ModelSerializer):
    selected_quiz = QuestionSerializers(many=True, read_only=True)
    category = serializers.StringRelatedField(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Quiz
        fields = ['title', 'category', 'created_by', 'img', 'grade',
                  'times_played', "likes", 'created_at', 'selected_quiz']



class HomePageSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)
    class Meta:
        model = Quiz
        fields = ['category', 'title', 'img', 'question_count', 'times_played']



class ReportQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ReportQuestion
        fields = "__all__"