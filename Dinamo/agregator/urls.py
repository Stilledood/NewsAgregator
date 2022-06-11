from django.urls import path,re_path
from .views import ArticleList,ArticleDetails,GspArticlesList,ProsportArticlesList


urlpatterns=[
    re_path(r'^$',ArticleList.as_view(),name='article_list'),
    re_path(r'^(?P<pk>\d+)/$',ArticleDetails.as_view(),name='article_details'),
    re_path(r'gsp/$',GspArticlesList.as_view(),name='gsp_articles'),
    re_path(r'prosport/$',ProsportArticlesList.as_view(),name='prosport_articles'),
]