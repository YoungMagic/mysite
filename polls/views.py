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

logger = logging.getLogger(__name__)


# version 1
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    if request.method == 'GET':
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)






