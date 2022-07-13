from django.urls import re_path
from .views import Contact


urlpatterns=[
    re_path('^$',Contact.as_view(),name='contact'),
]