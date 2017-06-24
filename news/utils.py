from bs4 import BeautifulSoup


class Entry(object):
    def __init__(self, data):
        self.data = data

    def get_url(self):
        return self.data.get('link')

    def get_categories(self):
        categories = [tag['term'] for tag in self.data.get('tags', [])]
        return categories

    def get_author(self):
        return self.data['author']


class News(object):

    def __init__(self, html):
        self.data = BeautifulSoup(html, 'html.parser')
        self._clean_data()
        self.story_bodies = self.data.find_all("div", class_="story-body")

    def _clean_data(self):
        for promo in self.data.find_all(class_="newsletter-promo"):
            promo.decompose()

        for hidden in self.data.find_all(class_="visually-hidden"):
            hidden.decompose()

        for script in self.data(["script", "style"]):
            script.extract()

    def get_formatted_text(self):
        contents = [str(body) for body in self.story_bodies]
        return " ".join(contents)

    def get_plain_text(self):
        contents = [body.get_text() for body in self.story_bodies]
        return " ".join(contents)

    def get_author(self):
        author = self.data.find_all("span", class_="byline-author")[0]
        return author.text
