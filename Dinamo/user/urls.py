from django.urls import path,re_path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView,PasswordChangeDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

app_name='user'
urlpatterns=[
    re_path(r'^$',RedirectView.as_view(pattern_name='dj-auth:login',permanent=False)),
    re_path(r'^login/$',LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    re_path(r'^logout/$',LogoutView.as_view(template_name='user/logout.html',extra_context={'fomr':AuthenticationForm}),name='logout')
]