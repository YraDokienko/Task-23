from django.test import TestCase
from django.urls import resolve, reverse


class PizzaTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_page_pizza_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pizza_home.html')
        self.assertContains(response, 'АМЕРИКАНО')

    def test_page_pizza_form_add(self):
        response = self.client.get('/pizza-form-add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form_pizza_add.html')

    def test_page_pizza_price_update(self):
        response = self.client.get('/pizza-price-update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pizza_price_update.html')

    def test_page_pizza_edit(self):
        url = reverse('pizza_update', args=[75])
        self.assertEqual(url, '/pizza-update/75/edit/')
        resol = resolve(url)
        self.assertEqual(resol.view_name, 'pizza_update')
