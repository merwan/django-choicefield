from django.test import TestCase

from myapp.models import TopLevelDomain


class TopLevelDomainTest(TestCase):

    def test_saving_and_retrieving_tlds(self):
        tlds = TopLevelDomain.objects.all()

        self.assertEqual(tlds.count(), 0)
