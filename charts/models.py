# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text

class ECoG(models.Model):
    Time = models.DateTimeField('date published')
    Value1 = models.IntegerField(default = 0)
    Value2 = models.IntegerField(default = 0)
    Value3 = models.IntegerField(default = 0)
    Value4 = models.IntegerField(default = 0)
    Value5 = models.IntegerField(default = 0)
    Value6 = models.IntegerField(default = 0)
    Value7 = models.IntegerField(default = 0)
    Value8 = models.IntegerField(default = 0)
    Value9 = models.IntegerField(default = 0)
    Value10 = models.IntegerField(default = 0)
    # def __str__(self):
    #     return str(self.Time)
