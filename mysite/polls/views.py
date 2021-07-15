from django.http import HttpResponse

from .models import Questions, Choice
from polls.models import Choice
#from mysite.polls.models import Questions


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list]) # переборка всех 5 вопросов в цикле
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at question %s" % question_id
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)
