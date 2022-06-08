import feedparser
from dateutil import parser
from agregator.models import Article
from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.conf import settings



def save_new_articles(feed):
    feed_title=feed.channel.title
    for item in feed.entries[:30]:
        if 'Dinamo' in item['title']:
                article=Article(title=item['title'],description=item['summary'],publishing_site=feed_title,publishing_date=parser.parse(item['published'][:-5]),link=item['link'],image=item['links'][1]['href'])
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
        scheduler.add_job(fetch_gsp_articles(),trigger='interval',minutes=2,id='Gsp Articles',max_instances=1,replace_existing=True)
        scheduler.add_job(fetch_prosport_article(),trigger='interval',minutes=2,id='Prosport Articles',max_instances=1,replace_existing=True)

        try:
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
            




