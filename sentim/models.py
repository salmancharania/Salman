from django.db import models

# Create your models here.

class Sentiment_Analyse(models.Model):
     sentiment_analyse=models.CharField(max_length=200)
     def _str_(self):
        return self.sentiment_analyse

class Twitter_Analyse(models.Model):
     twitter_analyse=models.CharField(max_length=200)
     def _str_(self):
        return self.twitter_analyse

class Word2vec_Analyse(models.Model):
     word2vec_analyse=models.CharField(max_length=200)
     def _str_(self):
        return self.word2vec
