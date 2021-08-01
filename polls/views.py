import logging

from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.cache import cache
from django.http import HttpResponse
# from .models import Question, Choice

logger = logging.getLogger(__name__)


# 请填入index视图函数





# 请取消注释以下代码
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     if request.method == 'GET':
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, 'polls/results.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))







