from django import forms
from .models import Answers,Comment

class CommentForm(forms.ModelForm):
    '''Class to construct a form for comment models'''

    class Meta:
        model=Comment
        fields=['body',]


class AnswerForm(forms.ModelForm):
    '''Class to construct a form for Answer Models'''

    class Meta:
        model=Answers
        fields=['body']
        
