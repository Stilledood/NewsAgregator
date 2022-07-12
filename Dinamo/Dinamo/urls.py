"""Dinamo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from agregator import urls as agg_urls
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from user import urls as user_urls
from forum import urls as forum_urls
from django.views.generic import RedirectView,TemplateView
from contact import urls as contact_urls
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',RedirectView.as_view(pattern_name='article_list',permanent=False)),
    re_path(r'^news/',include(agg_urls)),
    re_path(r'^user/',include(user_urls,namespace='dj-auth')),
    re_path(r'forum/',include(forum_urls)),
    re_path(r'^contact/',include(contact_urls)),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

admin.site.site_header='Dinamo News'
admin.site.site_title='Dinamo News'