import logging

from django.shortcuts import render, get_object_or_404

# Create your views here.


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question


logger = logging.getLogger(__name__)


# version 1
from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    if request.method == 'GET':
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
    if request.method == 'POST':
        """
        """
        return

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)











class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        cache_key = "index:v1:"
        # return Question.objects.filter(
        #         pub_date__lte=timezone.now()
        #     ).order_by('-pub_date')[:5]

        result = cache.get(cache_key)
        if not result:
            result = Question.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
            cache.set(cache_key, result, 60)
        return result




# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


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

# @cache_page(2)
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

from django.views import View


class ResultsView(View):

    def get(self, request, pk):

        question = get_object_or_404(Question, pk=pk)
        return render(request, 'polls/results.html', {'question': question})



