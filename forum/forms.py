from django import forms
from .models import Answers,Comment,Topics,Questions

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


class TopicForm(forms.ModelForm):
    '''Class to create a form for topic models'''

    class Meta:
        model=Topics
        fields=['title','short_description']

class QuestionForm(forms.ModelForm):
    '''Class to create a form for question models'''

    class Meta:
        model=Questions
        fields=['title']

