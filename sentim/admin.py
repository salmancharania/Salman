from django.contrib import admin
from .models import Sentiment_Analyse,Twitter_Analyse,Word2vec_Analyse
# Register your models here.

admin.site.register(Sentiment_Analyse)
admin.site.register(Twitter_Analyse)
admin.site.register(Word2vec_Analyse)
