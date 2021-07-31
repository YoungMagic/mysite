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


# version 1
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     if request.method == 'GET':
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, 'polls/results.html', {'question': question})
#
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)






