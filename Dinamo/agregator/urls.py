from django.urls import path,re_path
from .views import ArticleList,ArticleDetails


urlpatterns=[
    re_path(r'^$',ArticleList.as_view(),name='article_list'),
    re_path(r'^(?P<pk>\d+)/$',ArticleDetails.as_view(),name='article_details')
]