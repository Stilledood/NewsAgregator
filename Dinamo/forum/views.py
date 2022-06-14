from django.shortcuts import render,get_object_or_404,redirect
from .models import Topics,Answers,Questions,Comment
from django.views.generic import View


class GenericView(View):
    '''Class to construct a view to display forum first page-a mic of latest 5 Topics and last 5 questions'''

    template_name='forum/forum_view.html'

    def get(self,request):
        latest_topics=Topics.objects.all()[:5]
        latest_questions=Questions.objects.all()[:5]

        context={
            'topics':latest_topics,
            'questions':latest_questions
        }

        return render(request,self.template_name,context=context)

    



