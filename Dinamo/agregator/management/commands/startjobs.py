
import base64
import urllib.parse

import feedparser
import matplotlib.pyplot as plt
from dateutil import parser

from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.conf import settings
import regex as re
from agregator.models import Article
import pandas as pd
from datetime import timedelta,time,date
import io
from PIL import Image
from django.core.files.base import ContentFile
import os,shutil


def save_new_articles(feed):
    feed_title=feed.channel.title
    if feed_title == 'GSP.ro Fotbal':
        feed_title='GSP'

    for item in feed.entries[:30]:
        if 'Dinamo' in item['title']:
            if feed_title == 'GSP':
                guid_gsp=item['gsp_articol_id']
                if len(Article.objects.filter(guid=guid_gsp)) == 0:
                    article=Article(title=item['title'],description=item['summary'],publishing_site=feed_title,publishing_date=parser.parse(item['published'][:-5]),link=item['link'],image=item['links'][1]['href'],guid=item['gsp_articol_id'])
                    print(article.title)
                    article.save()
            elif feed_title == 'Prosport':
                x=item['id']
                m=re.match('.*?([0-9]+)$',x).group(1)
                if not Article.objects.filter(guid=m).exists():
                    article = Article(title=item['title'], description=item['summary'], publishing_site=feed_title,
                                      publishing_date=parser.parse(item['published'][:-5]), link=item['link'],
                                      image=item['links'][1]['href'], guid=m)
                    article.save()











def fetch_gsp_articles():
    _feed=feedparser.parse('https://www.gsp.ro/rss/fotbal-99.xml')
    save_new_articles(_feed)

def fetch_prosport_article():
    _feed=feedparser.parse('https://www.prosport.ro/feed')
    save_new_articles(_feed)




def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age=max_age)






class Command(BaseCommand):
    '''Custom command class to get all feed rss-uri from desired websites'''
    help='Runs apscheduler'

    def handle(self, *args, **options):
        scheduler=BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(),'default')
        scheduler.add_job(fetch_gsp_articles,trigger='interval',minutes=60,id='Gsp Articles',max_instances=1,replace_existing=True)
        scheduler.add_job(fetch_prosport_article,trigger='interval',minutes=60,id='Prosport Articles',max_instances=1,replace_existing=True)


        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()





