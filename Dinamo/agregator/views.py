from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from django.views import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import pandas as pd
import seaborn as sns
from datetime import datetime,date,timedelta
from plotly.offline import plot
from plotly.graph_objects import Scatter,Pie,Bar



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

class GraphView(View):

    '''Class to display some satistical graphs'''
    template_name='agregator/statistic.html'

    def get(self,request):

        dataframe=pd.DataFrame.from_records(Article.objects.all().values())
        dataframe['date']=pd.to_datetime(dataframe['publishing_date']).dt.date

        prev_week_start=date.today()-timedelta(weeks=1)
        this_week_dataframe=dataframe.loc[dataframe['date']>prev_week_start]['date'].value_counts().sort_index()
        plot_week=plot([Scatter(x=this_week_dataframe.index,y=this_week_dataframe.values,mode='lines',opacity=0.8,marker_color='green')],output_type='div')
        articles_week=this_week_dataframe.values.sum()


        last_month=date.today()-timedelta(weeks=4)
        this_month_data=dataframe.loc[dataframe['date']>last_month]['date'].value_counts().sort_index()
        this_month_plot=plot([Scatter(x=this_month_data.index,y=this_month_data.values,mode='lines',opacity=0.8,marker_color='red')],output_type='div')
        articles_month=this_month_data.values.sum()


        overall=dataframe['publishing_site'].value_counts()
        bar_chart=plot([Bar(x=['GSP','Prosport'],y=overall.values)],output_type='div')



        return render(request, self.template_name, context={'plot_week': plot_week,'plot_month':this_month_plot,'overall_plot':bar_chart,'nr_articles_week':articles_week,'nr_articles_month':articles_month})
