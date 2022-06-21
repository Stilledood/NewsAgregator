from .views import GenericView,TopicList,TopicDetails,QuestionList,QuestionDetails,AddTopic,EditTopic,EditQuestion,AddQuestion
from django.urls import re_path

urlpatterns=[
    re_path(r'^$',GenericView.as_view(),name='forum_generic'),
    re_path(r'^topics/$',TopicList.as_view(),name='topic_list'),
    re_path(r'^topics/(?P<pk>\d+)/$',TopicDetails.as_view(),name='topic_details'),
    re_path(r'^topics/(?P<pk>\d+)/edit/$',EditTopic.as_view(),name='topic_edit'),
    re_path(r'^questions/$',QuestionList.as_view(),name='question_list'),
    re_path(r'^questions/(?P<pk>\d+)/$',QuestionDetails.as_view(),name='question_details'),
    re_path(r'^questions/(?P<pk>\d+)/edit/$',EditQuestion.as_view(),name='question_edit'),
    re_path(r'topics/add/$',AddTopic.as_view(),name='topic_add'),
    re_path(r'questions/add/$',AddQuestion.as_view(),name='question_add'),
    ]

