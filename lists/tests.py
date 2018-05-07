from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.models import Item
from lists.views import home_page


class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(second_saved_item.text, '두 번째 아이템')

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
    
    def test_can_save_a_POST_request(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = '신규 작업 아이템'

        # response = home_page(request)

        # self.assertEqual(Item.objects.count(), 1)
        # new_item = Item.objects.first()
        # self.assertEqual(new_item.text, '신규 작업 아이템')

        ## 신규 예제 코드 - Processing a POST Request on the Server
        ## (https://www.obeythetestinggoat.com/book/chapter_post
        ## _and_database.html)
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = '신규 작업 아이템'

        # response = home_page(request)

        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/')

        ## 신규 예제 코드 - Better Unit Testing Practice: Each Test 
        ##               Should Test One Thing
        ## (https://www.obeythetestinggoat.com/book/chapter_post
        ## _and_database.html)
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_only_saves_items_when_necessary(self):
        # request = HttpRequest()
        # home_page(request)
        # self.assertEqual(Item.objects.count(), 0)

        ## 신규 예제 코드 - Saving the POST to the Database
        ## (https://www.obeythetestinggoat.com/book/
        ## chapter_post_and_database.html)
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')