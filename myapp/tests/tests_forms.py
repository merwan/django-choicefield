from django.test import TestCase

from myapp.forms import DomainForm
from myapp.models import TopLevelDomain


class DomainFormTest(TestCase):

    def setUp(self):
        TopLevelDomain.objects.create()

    def test_valid_data(self):
        form = DomainForm({
            'top_level_domain': 'fr'
        })

        self.assertTrue(form.is_valid())

    def test_top_level_domain_cannot_be_empty(self):
        form = DomainForm({
            'top_level_domain': ''
        })

        self.assertFalse(form.is_valid())
