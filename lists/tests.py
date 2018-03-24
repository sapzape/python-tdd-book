from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    # def test_root_url_resolve_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # def test_home_page_returns_correct_html(self):
    #     ## 기존 책 예제 코드
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     expected_html = render_to_string('home.html')
    #     self.assertEqual(html, expected_html)
        
    #     ## 신규 예제 코드 - The Django Test Client 
    #     ## (https://www.obeythetestinggoat.com/book/
    #     ##  chapter_philosophy_and_refactoring.html)
    #     # response = self.client.get('/')

    #     # html = response.content.decode('utf8')
    #     # self.assertTrue(html.startswith('<html>'))
    #     # self.assertIn('<title>To-Do lists</title>', html)
    #     # self.assertTrue(html.strip().endswith('</html>'))

    #     # self.assertTemplateUsed(response, 'home.html')
    #     ## self.assertTemplateUsed(response, 'wrong.html')

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')