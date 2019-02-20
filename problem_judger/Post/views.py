# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Question
from .models import Category
from django.db import models
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.utils.http import urlquote
import urllib.parse
from django.http import Http404
# Create your views here.

# 存储错题信息
class WrongAnswer:
    status = ""
    UAns = ""
    body =""
    answer = ""
    title = ""
    chioce_A = ""
    chioce_B = ""
    chioce_C = ""
    chioce_D = ""
class info:
    pass
def detail(request, category_name):
    #category_name = urllib.unquote(request.GET.get('category_name')).decode('utf8') #中文解码
    #category_name = urllib.parse.unquote(category_name)
    #question = get_object_or_404(Question, category=category_name)
    test_question = Question.objects.order_by('id')
    latest_question_list = []
    for question in test_question:
        if question.type_abbr==category_name:
            latest_question_list.append(question)

   # latest_question_list = get_object_or_404(Question, type_abbr=category_name) 
    return render(request, 'Post/detail.html', {'latest_question_list': latest_question_list})


def results(request, category_name):
    #category_name = urllib.unquote(request.GET.get('category_name')).decode('utf8') #中文解码
    #category_name = urllib.parse.unquote(category_name)
    latest_question_list = []
    test_question = Question.objects.order_by('id')
    for question in test_question:
        if question.type_abbr==category_name:
            latest_question_list.append(question)
    

    right = 0
    
    res = info()
    res.all = []
    for question in latest_question_list:
        if question.answer == request.POST[question.title]:
            right += 1
        else :
            wa = WrongAnswer()
            wa.status = "错误"
            wa.UAns = request.POST[question.title]
            wa.answer = question.answer
            wa.title = question.title
            wa.body = question.body
            wa.chioce_A = question.chioce_A
            wa.chioce_B = question.chioce_B
            wa.chioce_C = question.chioce_C
            wa.chioce_D = question.chioce_D
            res.all.append(wa)

    print(latest_question_list)
    
    res.right = right

    return render(request, 'Post/results.html', {'res': res})

def index(request):
    latest_category_list = Category.objects.order_by('name')
    template = loader.get_template('Post/index.html')
    context = {
        'latest_category_list': latest_category_list,
    }
    #context = urllib.unquote(request.GET.get('context')).decode('utf8')
    #context.name = urllib.parse.unquote(context.name)
    return HttpResponse(template.render(context, request))


