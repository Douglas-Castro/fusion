from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'name': "Fulano Beltrano",
            'email': "fulanobeltrano@fusion.com.br",
            'subject': "It's a test",
            'message': "Some message for me.", 
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'name': "Fulano Beltrano",
            'subject': "It's a test",
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)

