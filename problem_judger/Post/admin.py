# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question
from .models import Category
from .models import Tag

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Question)