from django.db import models
import datetime
from django.utils import timezone


class Category(models.Model):
    category_a = models.CharField(blank=True, null=True, max_length=100)
    category_b = models.CharField(blank=True, null=True, max_length=100)
    category_c = models.CharField(blank=True, null=True, max_length=100)
    category_d = models.CharField(blank=True, null=True, max_length=100)
    def __str__(self):
        return str(self.category_a)
    
class Money(models.Model):
    money_a = models.IntegerField(blank=True, null=True)
    money_b = models.IntegerField(blank=True, null=True)
    money_c = models.IntegerField(blank=True, null=True)
    money_d = models.IntegerField(blank=True, null=True)
    date = models.DateField('日付')
    
class Schedule(models.Model):
    
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.description
