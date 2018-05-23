from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from .models import Question, Choice
from django.http import Http404
from django.urls import reverse
from django.views import generic

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = '.'.join(q.question_text for q in latest_question_text)
    return render(request, 'html/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except:
        return Http404('this question no choice.')
    return render(request, 'html/detail.html', {'question': question})


def results(request, question_id):
    return render(request, 'html/results.html', {'question': Question.objects.get(id=question_id)})


def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    vote_id = request.POST.get('choice')
    try:
        choice = question.choice_set.get(id=vote_id)
        choice.votes += 1
        choice.save()
    except:
        return render(request, 'html/detail.html', {'question': question, 'error_message': 'you did not select a choice'})
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'html/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'html/detail.html'
    model = Question

class ResultsView(generic.DetailView):
    template_name = 'html/results.html'
    model = Question