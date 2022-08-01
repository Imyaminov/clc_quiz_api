from django.db import models
from helpers.models import BaseModel
from common.models import User
# Create your models here.

MULTIPLE_CHOICE = "multiple"
CHECKBOX = "checkbox"
FILL_IN_BLANK = "fill-in-the-blanks"
POLL = "poll"
OPEN_ENDED = "open-ended"
QUESTION_TYPE = (
    (MULTIPLE_CHOICE, "multiple"),
    (CHECKBOX, "checkbox"),
    (FILL_IN_BLANK, "fill-in-the-blanks"),
    (POLL, "poll"),
    (OPEN_ENDED, "open-ended"),
)

INAPPROPRIATE = 'inappropriate content'
INCORRECT = 'incorrect content'
OTHERS = 'others'
REPORT_ISSUE = (
    (INAPPROPRIATE, 'inappropriate content'),
    (INCORRECT, 'incorrect content'),
    (OTHERS, 'others'),
)

ELEMENTARY = 'elementary'
MIDDLE = 'middle'
HIGH = 'high'
UNIVERSITY = 'university'
ALL = 'all'
GRADE = (
    (ELEMENTARY, 'elementary school'),
    (MIDDLE, 'middle school'),
    (HIGH, 'high school'),
    (UNIVERSITY, 'university'),
    (ALL, 'all'),
)


class Category(BaseModel): # Subject
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    icon = models.FileField(upload_to="category/")

    def __str__(self):
        return str(self.title)


class Quiz(BaseModel):
    title = models.CharField(max_length=1024)
    img = models.ImageField(upload_to='quiz_img/', null=True)

    category = models.ManyToManyField(Category)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    grade = models.CharField(max_length=64, choices=GRADE)
    question_count = models.IntegerField(default=10)

    max_points = models.PositiveIntegerField(default=0)
    times_played = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    created_at = models.DateField(auto_now=True)
    duration = models.PositiveIntegerField(verbose_name='Quiz duration(sec)')

    def __str__(self):
        return f'{self.title}  {self.category}'


class Question(BaseModel):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='selected_quiz')
    title = models.TextField(
        max_length=256)
    type = models.CharField(
        max_length=32, choices=QUESTION_TYPE)

    show_answer = models.BooleanField(
        default=False)
    points = models.IntegerField(
        "Points per question", default=5)
    time = models.IntegerField(
        "Time(sec) per question", default=30)

    def __str__(self):
        return self.title


class QuestionOption(models.Model):
    title = models.CharField(max_length=256)
    is_correct = models.BooleanField(default=False)

    questions = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options")

    def __str__(self):
        return f'{self.title}  {self.questions}'


class ReportQuestion(BaseModel):
    issue = models.CharField(
        max_length=64, choices=REPORT_ISSUE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='report')
    additional = models.TextField(blank=True)


class StartQuiz(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now = False)

    is_finished = models.BooleanField(default=False)


class QuizAnswerStats(BaseModel):
    completed_quiz = models.ForeignKey(
        StartQuiz, on_delete=models.CASCADE, related_name='finished_quiz')
    rank = models.IntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    is_correct = models.BooleanField(default=False)

