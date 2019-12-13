from django.db import models
from django.forms import ModelForm
from django.conf import settings


class news(models.Model):
    news_name = models.CharField(max_length=50)
    news_text = models.TextField()

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

