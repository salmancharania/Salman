from django.shortcuts import render
from django.views import generic
from .models import Sentiment_Analyse, Twitter_Analyse, Word2vec_Analyse


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'sentim/index.html'

    def get_queryset1(self):
        return Sentiment_Analyse.objects.all()
    def get_queryset2(self):
        return Twitter_Analyse.objects.all()
    def get_queryset3(self):
        return Word2vec_Analyse.objects.all()

