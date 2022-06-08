import feedparser
from dateutil import parser
from agregator.models import Article
from django.core.management.base import BaseCommand



def save_new_articles(feed):
    feed_title=feed.channel.title
    for item in feed.entries[:30]:
        if 'Dinamo' in item['title']:
                article=Article(
                    title=item['title'],description=item['summary'],publishing_site=feed_title,publishing_date=item['published'][:-5],link=item['link'],image=
                )
                article.save()

def fetch_gsp_articles():
    _feed=feedparser.parse('https://www.gsp.ro/rss/fotbal-99.xml')
    save_new_articles(_feed)

def fetch_prosport_article():
    _feed=feedparser.parse('https://www.prosport.ro/feed')
    save_new_articles(_feed)








class Command(BaseCommand):
    '''Custom command class to get all feed rss-uri from desired websites'''

    def handle(self, *args, **options):
        fetch_gsp_articles()
        fetch_prosport_article()



