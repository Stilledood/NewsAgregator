from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.contrib.messages import success
from django.dispatch import receiver


@receiver(user_logged_in)
def display_login_message(sender,**kwargs):
    '''A function to display a succes message when user log in'''

    request=kwargs.get('request')
    user=kwargs.get('user')
    success(request,f'Succsfully logged in as {user.get_username()}',fail_silently=True)


@receiver(user_logged_out)
def display_logout_message(sender,**kwargs):
    '''A function to display a logout message'''

    request=kwargs.get('request')
    success(request,'Succsefully logged out',fail_silently=True)