from django.contrib import admin
from .models import *

# from django.apps import apps
# from django.contrib.auth.models import Group
#
# admin.site.unregister(Group)
# models = apps.get_models()
#
# for model in models:
#      admin.site.register(model)


# admin.site.register(Category)
# admin.site.register(Question)
# admin.site.register(QuestionOption)
admin.site.register(ReportQuestion)
admin.site.register(UserQuiz)
admin.site.register(UserQuizAnswer)
# admin.site.register(Quiz)

class QuestionInline(admin.TabularInline):
    model = Question
    fields = [
        'title',
        'type',
    ]

class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption
    fields = [
        'title',
        'is_correct'
    ]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        'title',
        'grade'
    ]
    inlines = [
        QuestionInline,
    ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        'type',
    ]
    list_display = [
        'title',
        'quiz'
    ]
    inlines = [
        QuestionOptionInline,
    ]

@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        'is_correct',
        'question',
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug'
    ]















