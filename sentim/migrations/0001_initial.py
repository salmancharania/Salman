# Generated by Django 3.1.7 on 2021-03-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment_Analyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment_analyse', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_Analyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_analyse', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Word2vec_Analyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word2vec_analyse', models.CharField(max_length=200)),
            ],
        ),
    ]