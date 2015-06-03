# from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import User


def index(request):
    user_list = User.objects.order_by('-name')[:5]
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('ums/index.html')
    context = RequestContext(request, {
        'user_list': user_list,
    })
    return HttpResponse(template.render(context))