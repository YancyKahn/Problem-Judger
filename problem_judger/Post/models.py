# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models    

class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=20)


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)


class Question(models.Model):
    """题目"""
    title = models.CharField(max_length=100)
    type_abbr = models.CharField(max_length=20, default="IDN")
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)  # 题目摘要，可为空
    category = models.ForeignKey(Category, on_delete=True)  # ForeignKey表示1对多（多个question对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)  # 阅读次数
    chioce_A = models.TextField(max_length=20)
    chioce_B = models.TextField(max_length=20)
    chioce_C = models.TextField(max_length=20)
    chioce_D = models.TextField(max_length=20)
    answer = models.TextField(max_length=10)
    
