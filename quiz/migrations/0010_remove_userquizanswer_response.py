# Generated by Django 4.0.6 on 2022-08-03 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_userquizanswer_is_correct_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquizanswer',
            name='response',
        ),
    ]