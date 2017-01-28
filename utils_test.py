import unittest
from utils import is_address


class TestStringMethods(unittest.TestCase):
    def test_is_address(self):
        self.assertTrue(is_address('Wickenburggasse 38-3a, 8010 Graz'))
        self.assertTrue(is_address('Propst Führer-Straße 4, 3100 Sankt Pölten'))
        self.assertTrue(is_address('Ignaz-Harrer-Straße 79, 5020 Salzburg'))
        self.assertFalse(is_address('Telefon: 13943'))
        self.assertFalse(is_address('THIS IS NOT AN ADDRESS'))
