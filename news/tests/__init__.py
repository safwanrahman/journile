import time

SAMPLE_ENTRY = {
    'title': 'U.N. to Investigate Reports of Government-Backed Slaughter in Congo',
    'title_detail': {
        'type': 'text/plain',
        'language': None,
        'base': 'http://rss.nytimes.com/services/xml/rss/nyt/Africa.xml',
        'value': 'U.N. to Investigate Reports of Government-Backed Slaughter in Congo'
    },
    'links': [{
        'rel': 'alternate',
        'type': 'text/html',
        'href': 'https://www.nytimes.com/2017/06/23/world/africa/congo-united-nations-human-rights-council.html?partner=rss&emc=rss'
    }, {
        'rel': 'standout',
        'href': 'https://www.nytimes.com/2017/06/23/world/africa/congo-united-nations-human-rights-council.html?partner=rss&emc=rss',
        'type': 'text/html'
    }],
    'link': 'https://www.nytimes.com/2017/06/23/world/africa/congo-united-nations-human-rights-council.html?partner=rss&emc=rss',
    'id': 'https://www.nytimes.com/2017/06/23/world/africa/congo-united-nations-human-rights-council.html',
    'guidislink': False,
    'summary': 'The United Nations’ human rights chief, Zeid Ra’ad al-Hussein, said even babies had been mutilated by a government-linked militia and insurgents.',
    'summary_detail': {
        'type': 'text/html',
        'language': None,
        'base': 'http://rss.nytimes.com/services/xml/rss/nyt/Africa.xml',
        'value': 'The United Nations’ human rights chief, Zeid Ra’ad al-Hussein, said even babies had been mutilated by a government-linked militia and insurgents.'
    },
    'authors': [{
        'name': 'NICK CUMMING-BRUCE'
    }],
    'author': 'NICK CUMMING-BRUCE',
    'author_detail': {
        'name': 'NICK CUMMING-BRUCE'
    },
    'published': 'Sat, 24 Jun 2017 09:02:09 GMT',
    'tags': [{
        'term': 'Congo, Democratic Republic of (Congo-Kinshasa)',
        'scheme': 'http://www.nytimes.com/namespaces/keywords/nyt_geo',
        'label': None
    }, {
        'term': 'United Nations Human Rights Council',
        'scheme': 'http://www.nytimes.com/namespaces/keywords/nyt_org_all',
        'label': None
    }, {
        'term': 'Human Rights and Human Rights Violations',
        'scheme': 'http://www.nytimes.com/namespaces/keywords/des',
        'label': None
    }, {
        'term': 'War Crimes, Genocide and Crimes Against Humanity',
        'scheme': 'http://www.nytimes.com/namespaces/keywords/des',
        'label': None
    }]
}


def get_sample_html():
    with open("test.html", "r") as file:
        return file.read()

