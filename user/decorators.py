from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required,permission_required
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured

def class_login_required(cls):
    '''Function to create a custom login required decorator to use on classes'''

    if (not isinstance(cls,type) or not issubclass(cls,View)):
        raise ImproperlyConfigured('Custom login decorator must be applied on a subclass of type View')
    decorator=method_decorator(login_required())
    cls.dispatch=decorator(cls.dispatch)
    return cls



def class_permission_required(permission):
    '''Function to create a custom permission required decorator to use on classes'''

    def decorator(cls):
        if ( not isinstance(cls,type) and not issubclass(cls,View)):
            raise ImproperlyConfigured('Class_permission_required decorator must be applied on a subclass of View class')
        check_auth=method_decorator(login_required)
        check_perm=method_decorator(permission_required(permission,raise_exception=True))
        cls.dispatch=check_auth(check_perm(cls.dispatch))
        return cls

    return decorator




