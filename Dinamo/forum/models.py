from django.db import models
from django.shortcuts import reverse
from django.conf import settings

class Topics(models.Model):
    '''Class to construct a model for admins added topics'''

    title=models.CharField(max_length=256)
    date_added=models.DateField(auto_now_add=True)
    posted_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_added','title']
        get_latest_by='date_added'

    def __str__(self):
        if len(self.title) > 30:
            return self.title[:30]
        return self.title

    def get_absolute_url(self):
        return reverse('topic_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('topic_update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('topic_delete',kwargs={'pk':self.pk})


class Comment(models.Model):
    '''Class to construct a model for topic comments'''

    body=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    topic=models.ForeignKey(Topics,on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_added']
        get_latest_by='date_added'

    def __str__(self):
        if len(self.body)>30:
            return self.body[:30]
        return self.body

    def get_update_url(self):
        return reverse('comment_update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('comment_delete',kwargs={'pk':self.pk})


class Questions(models.Model):
    '''Class to construct amodel for user forum question's'''

    title=models.CharField(max_length=256)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['-date_added','title']
        get_latest_by='date_added'

    def __str__(self):
        if len(self.title) > 30:
            return self.title[:30]
        return self.title

    def get_absolute_url(self):
        return reverse('question_details',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('question_delete',kwargs={'pk':self.pk})


class Answers(models.Model):
    '''Class to construct a model for question answers'''

    body=models.TextField()
    date_added=models.DateField(auto_now_add=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_added']
        get_latest_by='date_added'

    def __str__(self):
        if len(self.body) >30:
            return self.body[:30]
        return self.body

    def get_update_url(self):
        return reverse('answer_update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('question-delete',kwargs={'pk':self.pk})





