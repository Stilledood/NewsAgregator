from django.db import models
from django.shortcuts import redirect,render,get_object_or_404,reverse
from django.conf import settings



class Article(models.Model):
    '''Class to create a model for all news article'''

    title=models.TextField()
    image=models.ImageField(upload_to='news_images')
    description=models.TextField()
    publishing_site=models.TextField()
    publishing_date=models.DateTimeField()
    link=models.URLField(max_length=1000)
    guid=models.TextField()



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





