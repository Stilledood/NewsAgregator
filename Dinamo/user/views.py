from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.conf import settings
from django.views.generic import View
from django.contrib.auth import get_user,logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ProfileForm
from .models import Profile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .tokens import accountactivationtoken
from django.contrib import messages
from django.contrib.auth.models import User

class DisableUser(View):
    '''Class to construct a view to disable user account'''
    success_url=settings.LOGIN_REDIRECT_URL
    template_name='user/disable_account.html'

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def get(self,request):
        return TemplateResponse(request,self.template_name)


    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def post(self,request):
        user=get_user(request)
        user.set_unusable_password()
        user.is_active=False
        user.save()
        logout(request)
        return  redirect(self.success_url)



class SignUp(View):
    '''Class to construct a view for SIgn Up Process'''

    form_class=SignUpForm
    template_name='user/signup.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            user=bound_form.save(commit=False)
            user.is_active=False
            user.save()
            Profile.objects.update_or_create(user=user,defaults={'username':user.get_username()})
            current_site=get_current_site(request)
            subject='Activate Your account'
            message=render_to_string('user/account_activation_email.html',{'user':user,'domain':current_site.domain,'uid':urlsafe_base64_encode(force_bytes(user.pk)),'token':accountactivationtoken.make_token(user)})
            user.email_user(subject,message)
            messages.success(request,'Please confirm your email')
            return redirect('dj-auth:login')
        else:
            return  render(request,self.template_name,{'form':bound_form})


class AccountActivation(View):
    '''Class to create a view to verify email link and activate account'''

    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except (TypeError,ValueError,OverflowError):
            user=None

        if user != None and accountactivationtoken.check_token(user,token):
            user.is_active=True
            user.profile.email_confirmed=True
            user.save()
            Profile.objects.update_or_create(user=user,defaults={' '})
            return redirect('dj-auth:login')
        else:
            messages.warning(request,'Confirmation link isa no longer available')
            return  redirect('dj-auth:signup')

class ProfileDetails(View):
    '''Class to construct a view to see all profile details'''

    model=Profile
    template_name='user/profile.html'

    def get(self,request,username):
        profile=get_object_or_404(self.model,username=username)
        print(profile.image)
        return render(request,self.template_name,{'profile':profile})


class ProfileUpdate(View):
    '''Class to construct a view to allow a user to change his/her profile details'''

    model=Profile
    form_class=ProfileForm
    template_name='user/profile_update.html'

    def get(self,request,username):
        profile=get_object_or_404(self.model,username=username)
        return render(request,self.template_name,{'profile':profile,'form':self.form_class(instance=profile)})

    def post(self,request,username):
        profile=get_object_or_404(self.model,username=username)
        bound_form=self.form_class(request.POST,request.FILES,instance=profile)
        if bound_form.is_valid():
            new_profile = bound_form.save()



            return redirect(new_profile.get_absolute_url())
        else:
            return render(request,self.template_name,{'profile':profile,'form':bound_form})

