from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django .shortcuts import import render
class HomePageTest(TestCase):g
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)