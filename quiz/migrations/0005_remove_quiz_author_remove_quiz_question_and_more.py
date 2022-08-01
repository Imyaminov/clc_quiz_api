# Generated by Django 4.0.6 on 2022-07-31 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0004_quiz_max_points_startquiz_quizanswerstats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='author',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.RemoveField(
            model_name='quizanswerstats',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='startquiz',
            name='score',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='selected_quiz', to='quiz.quiz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizanswerstats',
            name='completed_quiz',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='finished_quiz', to='quiz.startquiz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizanswerstats',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quizanswerstats',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quizanswerstats',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='startquiz',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
