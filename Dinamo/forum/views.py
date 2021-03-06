from django.shortcuts import render,get_object_or_404,redirect
from .models import Topics,Answers,Questions,Comment
from django.views.generic import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CommentForm,AnswerForm,TopicForm,QuestionForm
from user.decorators import class_login_required,class_permission_required
from django.utils.decorators import  method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user


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
    @method_decorator(login_required)
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


@class_permission_required('forum.add_topics')
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


@class_permission_required('forum.change_topic')
class EditTopic(View):
    '''Class to construct a view to edit a topic'''

    model=Topics
    form_class=TopicForm
    template_name='forum/edit_topic.html'

    def get(self,request,pk):
        topic=get_object_or_404(self.model,pk=pk)
        context={
            'topic':topic,
            'form':self.form_class(instance=topic)
        }
        return render(request,self.template_name,context=context)

    def post(self,request,pk):
        topic=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST,instance=topic)
        if bound_form.is_valid():
            edited_topic=bound_form.save()
            return redirect(edited_topic.get_absolute_url())
        else:
            context={
                'topic':topic,
                'form':bound_form
            }

            return render(request,self.template_name,context=context)




class QuestionList(View):
    '''Class to display all questions '''

    template_name = 'forum/question_list.html'
    model = Questions
    page_kwargs = 'page'
    paginated_by = 10

    def get(self, request):
        questions = self.model.objects.all()
        paginator = Paginator(questions, self.paginated_by)
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
            'questions': page,
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
            'question': topic,
            'form': self.form_class()
        }

        return render(request, self.template_name, context=context)
    @method_decorator(login_required)
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
            return render(request, self.template_name, {'question': question, 'form': bound_form})


@class_login_required
class AddQuestion(View):
    '''Class to construct a view so the users can add questions to the site'''

    template_name='forum/add_question.html'
    form_class=QuestionForm
    model=Questions

    def get(self,request):
        latest_questions=self.model.objects.all()[:5]
        return render(request,self.template_name,{'form':self.form_class(),'latest':latest_questions})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            new_question=bound_form.save(commit=False)
            new_question.author=self.request.user
            new_question.save()
            return redirect(new_question.get_absolute_url())


class EditQuestion(View):
    '''Class to construct a view to let user update their own questions'''

    template_name='forum/edit_question.html'
    model_name=Questions
    form_class=QuestionForm

    def get(self,request,pk):
        question=get_object_or_404(self.model,pk=pk)
        return render(request,self.template_name,{'form':self.form_class(instance=question),'question':question})

    def post(self,request,pk):
        question=get_object_or_404(self.model_name,pk=pk)
        bound_form=self.form_class(request.POST,instance=question)
        if bound_form.is_valid():
            updated_question=bound_form.save()
            return redirect(updated_question.get_absolute_url())
        else:
            context={
                'question':question,
                'form':bound_form
            }

            return render(request,self.template_name,context=context)

