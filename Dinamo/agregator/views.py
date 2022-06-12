from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Comment
from django.views import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CommentForm
import pandas as pd
import seaborn as sns



class ArticleList(View):
    '''Class to construct a view to display all articles from data base using pagination(5 elements on a page)'''


    template_name='agregator/article_list.html'
    model=Article
    paginated_by=5
    page_kwargs='page'

    def get(self,request):
        article_list=self.model.objects.all()

        paginator=Paginator(article_list,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)
        try:
            page=paginator.page(page_number)
        except EmptyPage:
            page=paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            page=paginator.page(1)

        if page.has_previous():
            previous_page_url=f"?{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url=None

        if page.has_next():
            next_page_url=f"?{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url=None

        context={
            'article_list':page,
            'paginator':paginator,
            'next_page_url':next_page_url,
            'previous_page_url':previous_page_url
        }

        return render(request,self.template_name,context=context)



class ArticleDetails(View):
    '''Class to construct a view to display details about an article'''

    model=Article
    template_name='agregator/article_details.html'
    form_class=CommentForm

    def get(self,request,pk):
        article=get_object_or_404(self.model,pk=pk)
        context={
            'article':article,
            'form':self.form_class(),
            'next_article':next_article_pk,
            'previous_article':previous_article_pk
        }
        return render(request,self.template_name,context=context)

    def post(self,request,pk):
        article=get_object_or_404(self.model,pk=pk)
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            comm=bound_form.save(commit=False)
            comm.article=article
            comm.author=self.request.user
            comm.save()
            return  redirect(article.get_absolute_url())
        else:
            context={
                'article':article,
                'form':bound_form
            }
            return render(request,self.template_name,context=context)


class GspArticlesList(View):
    '''Class to display only GSP articles'''
    template_name='agregator/gsp_articles.html'
    model=Article
    page_kwargs='page'
    paginated_by=5


    def get(self,request):
        articles=self.model.objects.filter(publishing_site='GSP')
        paginator=Paginator(articles,self.paginated_by)
        page_number=request.GET.get(self.page_kwargs)

        try:
            page=paginator.page(page_number)
        except EmptyPage:
            page=paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            page=paginator.page(1)

        if page.has_previous():
            previous_page_url=f"?{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url=None

        if page.has_next():
            next_page_url=f"?{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url=None

        context={
            'article_list':page,
            'paginator':paginator,
            'previous_page_url':previous_page_url,
            'next_page_url':next_page_url,
        }

        return render(request,self.template_name,context=context)


class ProsportArticlesList(View):
    '''Class to display only Prosport articles'''
    template_name = 'agregator/prosport_articles.html'
    model = Article
    page_kwargs = 'page'
    paginated_by = 5

    def get(self, request):
        articles = self.model.objects.filter(publishing_site='Prosport')
        paginator = Paginator(articles, self.paginated_by)
        page_number = request.GET.get(self.page_kwargs)

        try:
            page = paginator.page(page_number)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            page = paginator.page(1)

        if page.has_previous():
            previous_page_url = f"?{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url = None

        if page.has_next():
            next_page_url = f"?{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url = None

        context = {
            'article_list': page,
            'paginator': paginator,
            'previous_page_url': previous_page_url,
            'next_page_url': next_page_url,
        }

        return render(request, self.template_name, context=context)





