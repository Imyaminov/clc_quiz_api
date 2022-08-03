# Generated by Django 4.0.6 on 2022-08-03 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0006_remove_startquiz_finished_at_alter_question_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('score', models.PositiveIntegerField(default=0)),
                ('is_finished', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='quiz.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='questionoption',
            old_name='questions',
            new_name='question',
        ),
        migrations.CreateModel(
            name='UserQuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_ids', models.CharField(max_length=255, null=True)),
                ('answered', models.BooleanField(default=False)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('user_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.userquiz')),
            ],
        ),
        migrations.AlterField(
            model_name='quizanswerstats',
            name='completed_quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finished_quiz', to='quiz.userquiz'),
        ),
        migrations.DeleteModel(
            name='StartQuiz',
        ),
    ]
