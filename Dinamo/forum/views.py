from django.shortcuts import render,get_object_or_404,redirect
from .models import Topics,Answers,Questions,Comment
from django.views.generic import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CommentForm,AnswerForm,TopicForm,QuestionForm


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
    form_class=CommentForm

    def get(self,request,pk):
        topic=get_object_or_404(self.model,pk=pk)
        context={
            'topic':topic,
            'form':self.form_class()
        }

        return render(request,self.template_name,context=context)

    def post(self,request,pk):
        topic=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_comm=bound_form.save(commit=False)
            new_comm.topic=topic
            new_comm.author=self.request.user
            new_comm.save()
            return redirect(topic.get_absolute_url())
        else:
            return render(request,self.template_name,{'topic':topic,'form':bound_form})

class AddTopic(View):
    '''Class to construct a view to add topic objects'''

    template_name='forum/add_topic.html'
    form_class=TopicForm

    def get(self,request):
        return render(request,self.template_name,context={'form':self.form_class})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_topic=bound_form.save(commit=False)
            new_topic.posted_by=self.request.user
            new_topic.save()
            return redirect(new_topic.get_absolute_url())
        else:
            return render(request,self.template_name,{'form':bound_form})



class QuestionList(View):
    '''Class to display all questions '''

    template_name = 'forum/question_list.html'
    model = Questions
    page_kwargs = 'page'
    paginated_by = 10

    def get(self, request):
        topics = self.model.objects.all()
        paginator = Paginator(topics, self.paginated_by)
        page_number = request.GET.get(self.page_kwargs)

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        if page.has_previous():
            previous_page_url = f"?{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url = None

        if page.has_next():
            next_page_url = f"?{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url = None

        context = {
            'topics': page,
            'paginator': paginator,
            'previous_page_url': previous_page_url,
            'next_page_url': next_page_url
        }

        return render(request, self.template_name, context=context)


class QuestionDetails(View):
    '''Class to create a view to display details of a question'''

    template_name = 'forum/question_details.html'
    model = Questions
    form_class = AnswerForm

    def get(self, request, pk):
        topic = get_object_or_404(self.model, pk=pk)
        context = {
            'topic': topic,
            'form': self.form_class()
        }

        return render(request, self.template_name, context=context)

    def post(self, request, pk):
        question = get_object_or_404(self.model, pk=pk)
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_answer= bound_form.save(commit=False)
            new_answer.question = question
            new_answer.author = self.request.user
            new_answer.save()
            return redirect(question.get_absolute_url())
        else:
            return render(request, self.template_name, {'topic': question, 'form': bound_form})

class AddQuestion(View):
    '''Class to construct a view so the users can add questions to the site'''

    template_name='forum/add_question.html'
    form_class=QuestionForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_question=bound_form.save(commit=False)
            new_question.author=self.request.user
            new_question.save()
            return redirect(new_question.get_absolute_url())
        