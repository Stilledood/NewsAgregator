from django.urls import path
from .views import ArticleList,ArticleDetails


urlpatterns=[
    path(r'^$',ArticleList.as_view(),name='article_list'),
    path('^(?P<pk>\d+)/$',ArticleDetails.as_view(),name='article_details')
]