import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEquals(str(self.service), self.service.service)


class PositionTestCase(TestCase):

    def setUp(self):
        self.position = mommy.make('Position')

    def test_str(self):
        self.assertEquals(str(self.position), self.position.position)


class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = mommy.make('Employee')

    def test_str(self):
        self.assertEquals(str(self.employee), self.employee.name)


class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature = mommy.make('Feature')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.title)


class PlanTestCase(TestCase):

    def setUp(self):
        self.plan = mommy.make('Plan')

    def test_str(self):
        self.assertEquals(str(self.plan), self.plan.name)


class ClientTestCase(TestCase):

    def setUp(self):
        self.client = mommy.make('Client')

    def test_str(self):
        self.assertEquals(str(self.client), self.client.name)

