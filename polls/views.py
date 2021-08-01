import logging

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.cache import cache
from django.http import HttpResponse
from .models import Question, Choice

logger = logging.getLogger(__name__)


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    # 排序时用-号表示倒叙
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# version 2
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    if request.method == 'GET':
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



