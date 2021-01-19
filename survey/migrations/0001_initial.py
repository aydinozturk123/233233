# Generated by Django 3.1.5 on 2021-01-10 13:38

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answertext', models.CharField(blank=True, db_column='AnswerText', max_length=10000, null=True, verbose_name='Answer')),
                ('surveyid', models.IntegerField(blank=True, db_column='SurveyID', null=True, verbose_name='Survey ID')),
                ('userid', models.IntegerField(blank=True, db_column='UserID', null=True, verbose_name='User ID')),
                ('questionid', models.IntegerField(blank=True, db_column='QuestionID', null=True, verbose_name='Question ID')),
                ('answerid', models.IntegerField(blank=True, db_column='AnswerID', primary_key=True, serialize=False, verbose_name='Answer ID')),
            ],
            options={
                'db_table': 'Answer',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questiontext', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Question')),
                ('questionid', models.IntegerField(blank=True, primary_key=True, serialize=False, verbose_name='Question ID')),
            ],
            options={
                'db_table': 'Question',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('surveyid', models.AutoField(db_column='SurveyID', primary_key=True, serialize=False, verbose_name='Survey ID')),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'Survey',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
