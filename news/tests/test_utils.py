from django.test import TestCase

from news.tests import SAMPLE_ENTRY

from ..utils import Entry


class EntryTest(TestCase):

    def setUp(self):
        self.entry = Entry(SAMPLE_ENTRY)

    def test_link(self):
        url = "https://www.nytimes.com/2017/06/23/world/africa/congo-united-nations-human-rights-council.html?partner=rss&emc=rss"
        self.assertEqual(self.entry.get_url(), url)

    def test_categories(self):
        categories = ['Congo, Democratic Republic of (Congo-Kinshasa)', 'United Nations Human Rights Council',
                      'Human Rights and Human Rights Violations', 'War Crimes, Genocide and Crimes Against Humanity']

        self.assertEqual(sorted(self.entry.get_categories()), sorted(categories))

    def test_author(self):
        self.assertEqual(self.entry.get_author(), "NICK CUMMING-BRUCE")


# class NewsTest(TestCase):
