from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question
from django.views import generic
from rest_framework.generics import ListCreateAPIView
from .serializers import *

# 함수형 뷰
# def index(request):
#     latest_question_list = Question.objects.order_by("pub_date")
#     return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice = question.choice_set.get(pk=request.POST['choice'])

    choice.votes += 1
    choice.save()

    return HttpResponseRedirect('result')


#RESTAPI
class ApiQuestionList(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
