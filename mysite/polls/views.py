from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])

    return HttpResponse(output)


def details(request, question_id):
    return HttpResponse("You are looking for at question %s" % question_id)


def results(request, question_id):
    response = "You are looking results at the question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
