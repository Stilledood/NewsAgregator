from django.shortcuts import render,redirect
from .forms import ContactForm
from django.views.generic import View
from django.contrib.messages import success
from forum.models import Topics



class Contact(View):
    '''Class to construct a view to allow user to send emails'''

    form_class=ContactForm
    template_name='contact/contact.html'
    topic_model=Topics

    def get(self,request):
        topics=self.topic_model.objects.all()[:5]
        return render(request,self.template_name,{'form':self.form_class,'topics':topics})

    def post(self,request):
        topics = self.topic_model.objects.all()[:5]
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():

            mail_sent=bound_form.send_email()
            if mail_sent:
                success(request,'Email successfully sent ')
                return redirect('article_list')
        else:
            return render(request,self.template_name,{'form':bound_form,'topics':topics})






