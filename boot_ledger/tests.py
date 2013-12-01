"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

from boot_ledger.models import Item

class ItemTests(TestCase):
	"""Item model test"""

	def test_str(self):

		item = Item(distributor='Epic Wines', category='Wine', sub_category='White',
		name='Pugliny', year='2009', country='France', region='Burgundy')

		self.assertEquals(
			str(item),
			'Epic Wines  Wine  White  Pugliny  2009  France  Burgundy'
		)

