from django.test import SimpleTestCase
from django.urls import reverse, resolve
# from we

class TestUrls(SimpleTestCase):


    def welcome_url_is_resolved(self):

        url = reverse('welcome')
        print(resolve(url))