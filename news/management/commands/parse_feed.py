import feedparser
import requests
from django.core.management.base import BaseCommand, CommandError

from news.models import Article
from news.utils import Entry, News


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "http://rss.nytimes.com/services/xml/rss/nyt/Africa.xml"
        feed = feedparser.parse(url)
        raw_entries = feed.entries

        for raw_entry in raw_entries:
            entry = Entry(raw_entry)
            request = requests.get(entry.get_url())
            news = News(request.content)
            article = Article.objects.create(formatted_text=news.get_formatted_text(),
                                             plain_text=news.get_plain_text(),
                                             author=entry.get_author() or news.get_author())

            categories = " ".join(entry.get_categories())

            article.categories.add(categories)
