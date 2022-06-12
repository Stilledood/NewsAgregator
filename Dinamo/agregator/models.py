from django.db import models
from django.shortcuts import redirect,render,get_object_or_404,reverse
from django.conf import settings



class Article(models.Model):
    '''Class to create a model for all news article'''

    title=models.CharField(max_length=256)
    image=models.ImageField(upload_to='news_images')
    description=models.TextField()
    publishing_site=models.CharField(max_length=128)
    publishing_date=models.DateField()
    link=models.URLField(max_length=256)
    guid=models.CharField(max_length=50)



    class Meta:
        ordering=['-publishing_date','title']
        get_latest_by='publishing_date'

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('article_details',kwargs={'pk':self.pk})

    def get_update_url(self):
        return reverse('article_update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('article_delete',kwargs={'pk':self.pk})

class Comment(models.Model):
    '''Class to construct a model for comments'''

    body=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    class Meta:
        ordering=['-date_added']
        get_latest_by='date_added'

    def __str__(self):
        if len(self.body)> 30:
            return self.body[:30]
        return self.body

    def get_delete_url(self):
        return reverse('delete_comment',kwargs={'pk':self.pk})



class Graph(models.Model):
    '''class to create models for statiscal graphs'''

    week_graphic=models.ImageField(upload_to='statistics/week')
    month_graph=models.ImageField(upload_to='statistics/month')
    gsp_vs_prosport=models.ImageField(upload_to='statistics/vs')
    overall=models.ImageField(upload_to='statistics/overall')


