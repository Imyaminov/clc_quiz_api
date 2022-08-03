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


class Category(BaseModel):  # Subject
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
        return f'{self.title}'

    def count(self):
        count = Question.objects.filter()


class Question(BaseModel):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='selected_quiz')
    title = models.CharField(max_length=2048)
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

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options")

    def __str__(self):
        return f'{self.title}'


class ReportQuestion(BaseModel):
    issue = models.CharField(
        max_length=64, choices=REPORT_ISSUE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='report')
    additional = models.TextField(blank=True)


class UserQuiz(BaseModel):
    """Quiz that User has taken"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    score = models.PositiveIntegerField(default=0)
    is_finished = models.BooleanField(default=False)

    def update_score(self):
        UserQuiz.objects.filter(id=self.id).update(
            score=UserQuizAnswer.objects.filter(is_correct=True, user_answer=self).count())

    def create_answers(self):
        quiz_answers = []
        for question in self.questions.all().order_by("?"):
            quiz_answers.append(UserQuizAnswer(
                user_answer=self, question=question))
        UserQuizAnswer.objects.bulk_create(quiz_answers)

class UserQuizAnswer(models.Model):
    """User answer to single question"""
    user_answer = models.ForeignKey(
        UserQuiz, on_delete=models.CASCADE, related_name="answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answered_question")
    response = models.ForeignKey(QuestionOption, on_delete=models.CASCADE, related_name='user_response', null=True)
    answered = models.BooleanField(default=False)

    @property
    def is_correct(self):
        correct_option = QuestionOption.objects.all().filter(question=self.question, is_correct=True)
        return correct_option == self.response.all()

