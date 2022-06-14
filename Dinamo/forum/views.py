from django.shortcuts import render,get_object_or_404,redirect
from .models import Topics,Answers,Questions,Comment
from django.views.generic import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


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


class TopicList(View):
    '''Class to create a view to  display all topics with pagination'''

    template_name='forum/topic_list.html'
    model=Topics
    page_kwargs='page'
    paginated_by=10

    def get(self,request):
        topics=self.model.objects.all()
        paginator=Paginator(topics,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)

        try:
            page=paginator.page(page_number)
        except PageNotAnInteger:
            page=paginator.page(1)
        except EmptyPage:
            page=paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url=f"?{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url=None

        if page.has_next():
            next_page_url=f"?{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url=None

        context={
            'topics':page,
            'paginator':paginator,
            'previous_page_url':previous_page_url,
            'next_page_url':next_page_url
        }

        return render(request,self.template_name,context=context)

class TopicDetails(View):
    '''Class to construct a view to see a topic details'''

    template_name='forum/topic_details.html'
    model=Topics



