from django.test import TestCase
from .models import Crate


class CrateModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Crate.objects.create(country='Kenya')
        Crate.objects.create(year='2020')

    def test_country_content(self):
        crate = Crate.objects.get(id=1)
        expected_object_name = f'{crate.country}'
        self.assertEquals(expected_object_name, 'Kenya')

    def test_year_content(self):
        crate = Crate.objects.get(id=2)
        expected_object_name = f'{crate.year}'
        self.assertEquals(expected_object_name, '2020')