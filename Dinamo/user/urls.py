from django.urls import path,re_path,include
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView,PasswordChangeDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordResetDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from .views import DisableUser

app_name='user'
password_urls=[
    re_path(r'^change/$',PasswordChangeView.as_view(template_name='user/password_change.html',success_url=reverse_lazy('dj-auth:password_change_done')),name='password_change'),
    re_path(r'^change/done/$',PasswordChangeDoneView.as_view(template_name='user/password_change_done.html',extra_context={'form':AuthenticationForm}),name='password_change_done'),
    re_path(r'^reset/$',PasswordResetView.as_view(template_name='user/password_reset.html' ,email_template_name='user/email_template.txt',subject_template_name='user/email_subject.txt' ,success_url=reverse_lazy('dj-auth:password_reset_done')),name='password_reset'),
    re_path(r'^reset/done/$',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',success_url=reverse_lazy('dj-auth:password_reset_complete')),name='password_reset_confirm'),
    re_path(r'reset/complete/$',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html',extra_context={'form':AuthenticationForm}),name='password_reset_complete'),


]

urlpatterns=[
    re_path(r'^$',RedirectView.as_view(pattern_name='dj-auth:login',permanent=False)),
    re_path(r'^login/$',LoginView.as_view(template_name='user/login.html',authentication_form=AuthenticationForm),name='login'),
    re_path(r'^logout/$',LogoutView.as_view(template_name='user/logout.html',extra_context={'fomr':AuthenticationForm}),name='logout'),
    re_path(r'^password/',include(password_urls)),
    re_path(r'disable_account/$',DisableUser.as_view(),name='disable_account'),

]